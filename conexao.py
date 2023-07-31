from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
database = client["openshift"]
collection = database["series"]