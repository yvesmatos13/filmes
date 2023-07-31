from pymongo import MongoClient
 
import json

with open("appsettings.json") as user_file:
  file_contents = user_file.read()

connectionStrings = json.loads(file_contents)

client = MongoClient(connectionStrings["ConnectionStrings"]["url"])
database = client[connectionStrings["ConnectionStrings"]["database"]]
collection = database[connectionStrings["ConnectionStrings"]["collection"]] 
