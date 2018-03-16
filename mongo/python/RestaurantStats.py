#!/usr/bin/env python3
from pymongo import MongoClient
import pprint
import pandas

# Create a MongoClient to the running mongo instance
client = MongoClient('mongodb://localhost:27017/')

# get the test database
db = client['test']
restaurants = db['restaurants']
pprint.pprint(restaurants.find_one())

cursor = db['restaurants'].find({})
dataframe = pandas.DataFrame(list(cursor))

print(dataframe)
