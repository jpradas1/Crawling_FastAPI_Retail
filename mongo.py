import json
from pymongo import MongoClient

# Read json files to create the database on MongoDB

with open('./dataset/puma.json', 'r') as json_file:
    puma = json.load(json_file)

with open('./dataset/adidas.json', 'r') as json_file:
    adidas = json.load(json_file)

# Creating a unique id for each item

for ii, product in enumerate(puma):
    product["id"] = ii

for ii, product in enumerate(adidas):
    product['id'] = ii + len(puma)

# Up MongoDB connection

client = MongoClient('mongodb://localhost:27017/')

# Defining the database 'products' and the collection 'item' where
# data is going to be allocated

products = client['products']
collection = products['items']

# Inserting both datasets, puma and adidas

inserted_puma = collection.insert_many(puma)
inserted_adidas = collection.insert_many(adidas)

client.close()