import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME")

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]
def get_user_collection():
    return db.users
def get_otp_collection():
    return db["password_otps"]
def get_place_collection():
    return db["places"]
def get_category_collection():
    return db["categories"]