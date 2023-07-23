from pymongo import MongoClient
import os

MONGO_URL = os.environ.get("MONGO_URL")
connection = MongoClient("{}".format(MONGO_URL))

# If you work locally, better use the following connection
# connection = MongoClient('mongodb://localhost:27017/')