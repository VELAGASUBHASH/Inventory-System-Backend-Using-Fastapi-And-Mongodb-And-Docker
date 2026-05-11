import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

Mongourl = os.getenv("MONGO_URL")
client = AsyncIOMotorClient(Mongourl)
db = client.Inventory_System
products_collection = db.products
