from pymongo import MongoClient

client = MongoClient("mongodb+srv://somnathroy0340:nWXgQlhalZzcS12X@cluster0.okzjo3u.mongodb.net/?retryWrites=true&w=majority")


db = client.FastAPI
collection_name1 = db["assets"]
collection_name2 = db["performancemetrics"]