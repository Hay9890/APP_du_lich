from fastapi import HTTPException
from passlib.context import CryptContext

from app.models.user import UserRegister, UserInDB, UserResponse

# dùng Argon2 thay vì bcrypt
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Hash password bằng Argon2
    Không bị giới hạn 72 bytes như bcrypt
    """
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Dùng cho login sau này
    """
    return pwd_context.verify(password, hashed_password)


async def register_user_controller(
    user: UserRegister,
    users_col
) -> UserResponse:

    # kiểm tra email tồn tại
    existing_user = await users_col.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # tạo user mới
    user_db = UserInDB(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    result = await users_col.insert_one(user_db.model_dump())

    # trả response
    return UserResponse(
        id=str(result.inserted_id),
        username=user.username,
        email=user.email
    )