from pymongo import MongoClient
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGO_URL: str

# Connection to railway.app database

setting = Settings()
MONGO_URL = setting.MONGO_URL
connection = MongoClient(MONGO_URL)

# If you work locally, better use the following connection
# connection = MongoClient('mongodb://localhost:27017/')