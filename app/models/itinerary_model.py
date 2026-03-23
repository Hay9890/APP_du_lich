from pydantic import BaseModel
from datetime import date, datetime

class ItineraryCreate(BaseModel):
    user_id: str
    location_id: str
    start_date: datetime
    end_date: datetime
    people: int
    budget: str
    travel_style: str
    companion: str


class ItineraryResponse(ItineraryCreate):
    id: str
    created_at: datetime