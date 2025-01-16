from pymongo import MongoClient

def get_db_connection():
    try:
        client = MongoClient('localhost', 27017,)
        db = client.testdb
        print("Connected to MongoDB")
        return db
    except Exception as e:
        print(e)
        exit(1)