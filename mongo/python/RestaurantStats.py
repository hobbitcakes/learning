#!/usr/bin/env python3
from pymongo import MongoClient
import pprint

# Create a MongoClient to the running mongo instance
client = MongoClient('mongodb://localhost:27017/')

# get the test database
db = client['test']
restaurant = db['restaurant']
pprint.pprint(restaurant.find_one())
