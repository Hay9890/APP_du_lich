from fastapi import APIRouter, Depends, status

from dependencies import get_user_collection
from app.models.user import UserRegister, UserResponse
from app.controllers.user.user import register_user_controller

router = APIRouter(prefix="/auth", tags=["User Auth"])


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
async def register_user(
    user: UserRegister,
    users_col=Depends(get_user_collection)
):
    return await register_user_controller(user, users_col)
