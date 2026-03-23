import os
from dotenv import load_dotenv
from datetime import datetime
from bson import ObjectId
from app.models.place_model import PlaceCreate, PlaceUpdate

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
        "thumbnail": (BASE_IMAGE_URL or "") + place["thumbnail"] if place.get("thumbnail") else None,
        "created_at": place["created_at"]
    }


async def create_place(data: PlaceCreate, collection):
    place = {
        "name": data.name,
        "description": data.description,
        "address": data.address,
        "city": data.city,
        "category_id": data.category_id,
        "thumbnail": data.thumbnail,  
        "created_at": datetime.utcnow()
    }

    result = await collection.insert_one(place)
    place["_id"] = result.inserted_id

    return serialize(place)



async def update_place(place_id: str, data: PlaceUpdate, collection):
    try:
        obj_id = ObjectId(place_id)
    except:
        return None

    
    update_data = {k: v for k, v in data.dict().items() if v is not None}

    if not update_data:
        return None

    result = await collection.update_one(
        {"_id": obj_id},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        return None

    updated_place = await collection.find_one({"_id": obj_id})
    return serialize(updated_place)


async def delete_place(place_id: str, collection):
    try:
        obj_id = ObjectId(place_id)
    except:
        return False

   
    place = await collection.find_one({"_id": obj_id})
    if not place:
        return False

   
    result = await collection.delete_one({"_id": obj_id})

    if result.deleted_count == 0:
        return False

    
    if place.get("thumbnail"):
        file_path = f"static/image/{place['thumbnail']}"
        if os.path.exists(file_path):
            os.remove(file_path)

    return True