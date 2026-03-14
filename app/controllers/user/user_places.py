import os
from dotenv import load_dotenv

load_dotenv()

BASE_IMAGE_URL = os.getenv("BASE_IMAGE_URL")


def serialize(place):
    return {
        "id": str(place["_id"]),
        "name": place["name"],
        "description": place.get("description"),
        "address": place["address"],
        "city": place["city"],
        "thumbnail": BASE_IMAGE_URL + place["thumbnail"],
        "created_at": place["created_at"]
    }


async def get_places(collection):

    places = await collection.find().to_list(100)

    return [serialize(place) for place in places]