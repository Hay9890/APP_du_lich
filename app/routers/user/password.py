from fastapi import APIRouter, Depends
from app.models.password_reset import (
    ForgotPasswordRequest,
    ResetPasswordRequest
)
from app.controllers.user.user_password_controller import (
    forgot_password_logic,
    reset_password_logic
)
from dependencies import get_user_collection, get_otp_collection

router = APIRouter(prefix="/auth", tags=["User Password"])


@router.post("/forgot")
async def forgot_password(
    data: ForgotPasswordRequest,
    users_col=Depends(get_user_collection),
    otp_col=Depends(get_otp_collection)
):
    await forgot_password_logic(data, users_col, otp_col)
    return {"message": "OTP sent to email"}


@router.post("/reset")
async def reset_password(
    data: ResetPasswordRequest,
    users_col=Depends(get_user_collection),
    otp_col=Depends(get_otp_collection)
):
    await reset_password_logic(data, users_col, otp_col)
    return {"message": "Password reset successful"}
