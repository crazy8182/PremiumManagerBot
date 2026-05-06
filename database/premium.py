from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

mongo = AsyncIOMotorClient(MONGO_URI)

db = mongo.PremiumBot

premium = db.premium
users = db.users

async def add_user(user_id):
    await users.update_one(
        {"user_id": user_id},
        {"$set": {"user_id": user_id}},
        upsert=True
    )

async def get_all_users():
    data = []
    async for x in users.find():
        data.append(x)
    return data

async def add_premium(user_id, name, plan, expiry):
    data = {
        "user_id": user_id,
        "name": name,
        "plan": plan,
        "expiry": expiry,
        "active": True
    }

    await premium.update_one(
        {"user_id": user_id},
        {"$set": data},
        upsert=True
    )

async def get_premium(user_id):
    return await premium.find_one({"user_id": user_id})

async def remove_premium(user_id):
    await premium.delete_one({"user_id": user_id})

async def get_all_premium():
    data = []
    async for x in premium.find():
        data.append(x)
    return data
