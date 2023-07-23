from pymongo import MongoClient
import os

# Connection to railway.app database
MONGO_URL = str(os.environ.get("MONGO_URL"))
connection = MongoClient(MONGO_URL)

# If you work locally, better use the following connection
# connection = MongoClient('mongodb://localhost:27017/')