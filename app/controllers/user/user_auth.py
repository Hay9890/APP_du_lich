from fastapi import HTTPException, status
from app.core.security import verify_password, create_access_token
from app.models.auth import UserLogin


async def login_user_logic(user: UserLogin, users_col):
    db_user = await users_col.find_one({"email": user.email})

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    token = create_access_token({
        "sub": str(db_user["_id"]),
        "role": db_user.get("role", "user")
    })

    return token
