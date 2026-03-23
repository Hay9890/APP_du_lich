from fastapi import APIRouter, Depends
from app.controllers.admin import category_admin as category_ctrl
from app.models.category import CategoryCreate
from dependencies import get_category_collection

router = APIRouter(prefix="/categories", tags=["Admin Category"])


# CREATE CATEGORY
@router.post("/create")
async def create_category(
    data: CategoryCreate,
    collection=Depends(get_category_collection)
):
    return await category_ctrl.create_category(data, collection)
@router.get("/")
async def get_categories(
    collection=Depends(get_category_collection)
):
    return await category_ctrl.get_all_categories(collection)