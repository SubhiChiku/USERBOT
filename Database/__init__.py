from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from config import MONGO_URI

mongo = MongoClient(MONGO_URI)

db = mongo.RBX
