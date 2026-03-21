from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FavoriteCreate(BaseModel):
    user_id: str
    place_id: str


class FavoriteResponse(BaseModel):
    id: str
    user_id: str
    place_id: str
    created_at: datetime
    place_info: Optional[dict] = None 