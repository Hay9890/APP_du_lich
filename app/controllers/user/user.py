from fastapi import HTTPException
from passlib.context import CryptContext

from app.models.user import UserRegister, UserInDB, UserResponse

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    # bcrypt chỉ hỗ trợ tối đa 72 bytes
    safe_password = password.encode("utf-8")[:72].decode("utf-8", "ignore")
    return pwd_context.hash(safe_password)


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

    # tạo user trong database
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