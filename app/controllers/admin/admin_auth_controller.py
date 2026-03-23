from fastapi import HTTPException, status
from passlib.context import CryptContext
from app.models.admin import AdminLogin 
from app.core.security import create_access_token

pwd_context = CryptContext(
    schemes=["argon2", "bcrypt"],  
    deprecated="auto"
)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def admin_login_logic(data: AdminLogin, users_col):
    admin = await users_col.find_one({
        "email": data.email,
        "role": "admin"
    })

    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Admin not found"
        )

    if not verify_password(data.password, admin["password"]):  
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong password"
        )

    access_token = create_access_token({
        "sub": str(admin["_id"]),
        "role": "admin"
    })

    return {
        "id": str(admin["_id"]),
        "email": admin["email"],
        "role": admin["role"],
        "access_token": access_token,
        "token_type": "bearer"   
    }