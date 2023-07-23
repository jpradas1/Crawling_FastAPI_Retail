from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
connection = MongoClient("{}".format(MONGO_URL))

# If you work locally, better use the following connection
# connection = MongoClient('mongodb://localhost:27017/')