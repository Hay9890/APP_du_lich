from fastapi import APIRouter
from dependencies import get_place_collection
from app.controllers.user.user_places import get_places

router = APIRouter(prefix="/auth")

@router.get("/places")
async def get_all_places():

    place_collection = get_place_collection()

    return await get_places(place_collection)