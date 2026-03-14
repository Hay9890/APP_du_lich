import os
from dotenv import load_dotenv
from datetime import datetime
from bson import ObjectId
from app.models.place_model import PlaceCreate

load_dotenv()

BASE_IMAGE_URL = os.getenv("BASE_IMAGE_URL")

def serialize(place):
    return {
        "id": str(place["_id"]),
        "name": place["name"],
        "description": place.get("description"),
        "address": place["address"],
        "city": place["city"],
        "category_id": place["category_id"],
        "thumbnail": BASE_IMAGE_URL + place["thumbnail"],
        "created_at": place["created_at"]
    }