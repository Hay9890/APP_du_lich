from fastapi import APIRouter
from app.routers.user.register import router as user_register_router
from app.routers.user.auth import router as user_auth_router
from app.routers.user.password import router as password_router
from app.routers.user.places import router as user_places_router
router = APIRouter(prefix="/api")
router.include_router(user_register_router, prefix="/user")
router.include_router(user_auth_router,prefix="/user")
router.include_router(password_router, prefix="/user")
router.include_router(user_places_router,prefix="/user")

