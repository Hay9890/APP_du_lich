from datetime import datetime
from bson import ObjectId
from app.models.favorite_model import FavoriteCreate, FavoriteResponse
from app.controllers.admin.place_admin_controller import serialize as serialize_place

# Thêm favorite
async def Add_favorite(user_id: str, place_id: str, collection):
    existing = await collection.find_one({"user_id": user_id, "place_id": place_id})
    if existing:
        return {"message": "Already favorited"}

    data = {
        "user_id": user_id,
        "place_id": place_id,
        "created_at": datetime.utcnow()
    }

    result = await collection.insert_one(data)
    new_fav = await collection.find_one({"_id": result.inserted_id})
    new_fav["place_info"] = None
    return FavoriteResponse(
        id=str(new_fav["_id"]),
        user_id=new_fav["user_id"],
        place_id=new_fav["place_id"],
        created_at=new_fav["created_at"],
        place_info=None
    )

# Xóa favorite
async def Remove_favorite(user_id: str, place_id: str, collection):
    await collection.delete_one({"user_id": user_id, "place_id": place_id})
    return {"message": "Removed from favorites"}

# Lấy tất cả favorites của user kèm info place
async def get_user_favorites(user_id: str, fav_collection, place_collection):
    cursor = fav_collection.find({"user_id": user_id})
    result = []
    async for fav in cursor:
        place = await place_collection.find_one({"_id": ObjectId(fav["place_id"])})
        if place:
            place_data = serialize_place(place)
        else:
            place_data = None

        result.append(
            FavoriteResponse(
                id=str(fav["_id"]),
                user_id=fav["user_id"],
                place_id=fav["place_id"],
                created_at=fav["created_at"],
                place_info=place_data
            )
        )
    return result