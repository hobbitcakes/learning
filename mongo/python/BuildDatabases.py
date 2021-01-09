#!/usr/bin/env python3
from pymongo import MongoClient
import json

# Create a MongoClient to the running mongo instance
client = MongoClient('mongodb://localhost:27017/')

# get the test database
db_sample = client['sample']
db_sample_restaurant = db_sample['restaurant']

#dataset = {}
with open('primer-dataset.json') as data:
    for line in data:
        print(db_sample_restaurant.insert_one(json.loads(line)))


