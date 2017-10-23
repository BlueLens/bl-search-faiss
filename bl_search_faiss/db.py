# -*- coding: utf-8 -*-

from flask import Flask
from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

# HOST = 'localhost'
HOST = '35.198.213.52'
DB = 'bl-db-image'
client = MongoClient(HOST, 27017)
db = client[DB]
collection_images = db.images

def query_by_id(id):
  pprint(id)
  return collection_images.find_one({'_id': ObjectId(id)})
