from fastapi import APIRouter, Depends
from app.controllers.user import user_itinerary_controller as iti_ctrl
from app.models.itinerary_model import ItineraryCreate
from dependencies import get_itinerary_collection

router = APIRouter(prefix="/itineraries")


@router.post("/create")
async def create_itinerary(
    data: ItineraryCreate,
    collection=Depends(get_itinerary_collection)
):
    return await iti_ctrl.create_itinerary(data, collection)

@router.get("/get/{user_id}")
async def get_itineraries(
    user_id: str,
    collection=Depends(get_itinerary_collection)
):
    return await iti_ctrl.get_itineraries(user_id, collection)


@router.delete("/delete/{itinerary_id}")
async def delete_itinerary(
    itinerary_id: str,
    collection=Depends(get_itinerary_collection)
):
    return await iti_ctrl.delete_itinerary(itinerary_id, collection)