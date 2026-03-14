from fastapi import APIRouter, Depends
from dependencies import get_user_collection
from app.models.auth import UserLogin, TokenResponse
from app.controllers.user.user_auth import login_user_logic

router = APIRouter(prefix="/auth", tags=["User Auth"])


@router.post("/login", response_model=TokenResponse)
async def login(
    user: UserLogin,
    users_col=Depends(get_user_collection)
):
    token = await login_user_logic(user, users_col)
    return {
        "access_token": token,
        "token_type": "bearer"
    }
