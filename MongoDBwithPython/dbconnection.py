from pymongo import MongoClient
import os
mongo_host = os.getenv("MONGO_HOST", "localhost")
mongo_port = int(os.getenv("MONGO_PORT", 27017))

def get_db_connection():
    try:
        client = MongoClient(mongo_host, mongo_port)
        db = client.userdata
        print("Connected to MongoDB")
        return db
    except Exception as e:
        print(e)
        exit(1)