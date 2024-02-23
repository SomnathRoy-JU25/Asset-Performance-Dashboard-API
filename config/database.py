from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://somnathroy0340:nWXgQlhalZzcS12X@cluster0.okzjo3u.mongodb.net/?retryWrites=true&w=majority&appName=FastAPI"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Access the database
db = client.get_database("FastAPI")  # Replace "your_database_name" with your actual database name

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print(" You successfully connected to MongoDB! ")
except Exception as e:
    print(e)