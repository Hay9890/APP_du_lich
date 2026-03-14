from fastapi import APIRouter, Depends
from app.models.admin import AdminLogin, AdminResponse
from app.controllers.admin.admin_auth_controller import admin_login_logic
from dependencies import get_user_collection

router = APIRouter(prefix="/admin/auth", tags=["Admin Auth"])


@router.post("/login", response_model=AdminResponse)
async def admin_login(
    data: AdminLogin,
    users_col=Depends(get_user_collection)
):
    return await admin_login_logic(data, users_col)
