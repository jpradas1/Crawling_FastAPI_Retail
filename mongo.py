import bson
from pymongo import MongoClient
import os

'''This file is to create the dataset in a MongoDB server.'''

# Read bson file to create the database on MongoDB

with open('./dataset/Products/product_items.bson', 'rb') as bson_file:
    bson_data = bson_file.read()

decoded_data = bson.decode_all(bson_data)

# Up MongoDB connection

MONGO_URL = os.environ.get('MONGO_URL')
client = MongoClient(MONGO_URL)

# Defining the database 'products' and the collection 'item' where
# data is going to be allocated

products = client['Products']
collection = products['product_items']

# Inserting both datasets, puma and adidas

inserted_puma = collection.insert_many(decoded_data)

client.close()