from datetime import datetime
from bson import ObjectId


def serialize(itinerary):
    return {
        "id": str(itinerary["_id"]),
        "user_id": itinerary["user_id"],
        "location_id": itinerary["location_id"],
        "start_date": itinerary["start_date"],
        "end_date": itinerary["end_date"],
        "people": itinerary["people"],
        "budget": itinerary["budget"],
        "travel_style": itinerary["travel_style"],
        "companion": itinerary["companion"],
        "created_at": itinerary["created_at"]
    }


# CREATE ITINERARY
async def create_itinerary(data, collection):
    itinerary_data = data.dict()
    itinerary_data["created_at"] = datetime.utcnow()

    result = await collection.insert_one(itinerary_data)

    new_itinerary = await collection.find_one({
        "_id": result.inserted_id
    })

    return serialize(new_itinerary)


# GET USER ITINERARIES
async def get_itineraries(user_id: str, collection):
    cursor = collection.find({"user_id": user_id})

    result = []
    async for item in cursor:
        result.append(serialize(item))

    return result


# DELETE ITINERARY
async def delete_itinerary(itinerary_id: str, collection):
    await collection.delete_one({"_id": ObjectId(itinerary_id)})
    return {"message": "Deleted"}