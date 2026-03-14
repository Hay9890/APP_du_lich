from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class PlaceCreate(BaseModel):
    name:str
    description: Optional[str]=None
    address: str
    city:str
    category_id:str
    thumbnail:str
class PlaceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    thumbnail: Optional[str] = None
class Placeresponse(PlaceCreate):
    id: str
    created_at: datetime
  