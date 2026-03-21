from fastapi import APIRouter, Depends
from app.controllers.user.user_favorite_controller import (
    get_user_favorites,
    Add_favorite,
    Remove_favorite
)
from dependencies import get_favorite_collection, get_place_collection
from app.models.favorite_model import FavoriteCreate
router = APIRouter(prefix="/user", tags=["User Favorites"])


# ADD FAVORITE
@router.post("/favorites")
async def add_favorite(
    data: FavoriteCreate,
    collection=Depends(get_favorite_collection)
):
    return await Add_favorite(data.user_id, data.place_id, collection)


# REMOVE FAVORITE
@router.delete("/delete")
async def remove_favorite(
    data: FavoriteCreate,
    collection=Depends(get_favorite_collection)
):
    return await Remove_favorite(data.user_id, data.place_id, collection)


# GET FAVORITES
@router.get("/favorites/{user_id}")
async def get_favorites(
    user_id: str,
    fav_collection=Depends(get_favorite_collection),
    place_collection=Depends(get_place_collection)
):
    return await get_user_favorites(user_id, fav_collection, place_collection)