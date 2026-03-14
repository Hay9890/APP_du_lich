from bson import ObjectId
from app.models.category import CategoryCreate


def serialize(category):
    return {
        "id": str(category["_id"]),
        "name": category["name"]
    }


async def create_category(data: CategoryCreate, collection):

    category_data = data.dict()

    result = await collection.insert_one(category_data)

    new_category = await collection.find_one(
        {"_id": result.inserted_id}
    )

    return serialize(new_category)