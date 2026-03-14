from fastapi import HTTPException, status
from datetime import datetime, timedelta
from app.utils.otp import generate_otp
from app.utils.password import hash_password
from app.utils.mail import send_otp_email


# GỬI OTP
async def forgot_password_logic(data, users_col, otp_col):
    user = await users_col.find_one({"email": data.email})
    if not user:
        raise HTTPException(404, "Email not found")

    otp = generate_otp()
    expires_at = datetime.utcnow() + timedelta(minutes=5)

    await otp_col.delete_many({"email": data.email})

    await otp_col.insert_one({
        "email": data.email,
        "otp": otp,
        "expires_at": expires_at
    })

    send_otp_email(data.email, otp)


# RESET PASSWORD
async def reset_password_logic(data, users_col, otp_col):
    record = await otp_col.find_one({
        "email": data.email,
        "otp": data.otp
    })

    if not record:
        raise HTTPException(400, "Invalid OTP")

    if record["expires_at"] < datetime.utcnow():
        raise HTTPException(400, "OTP expired")

    await users_col.update_one(
        {"email": data.email},
        {"$set": {"hashed_password": hash_password(data.new_password)}}
    )

    await otp_col.delete_one({"_id": record["_id"]})
