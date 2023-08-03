from pymongo import MongoClient
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGO_URL: str = "mongodb://localhost:27017/"
    DATABASE: str = "Products"
    COLLECTION: str = "product_items"

# Connection to MongoDB database

setting = Settings()
MONGO_URL = setting.MONGO_URL
connection = MongoClient(MONGO_URL)
database = connection[setting.DATABASE]
collection = database[setting.COLLECTION]