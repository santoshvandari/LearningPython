from dbconnection import get_db_connection

db=get_db_connection()

def get_all_documents():
    return db.testcollection.find()

def insert_document(data):
    res=db.testcollection.insert_one(data)
    return res.inserted_id

def insert_many_documents(data):
    res=db.testcollection.insert_many(data)
    return res.inserted_ids



if __name__=="__main__":
    pattern = '''==============================================
    Welcome to MongoDB CRUD operations
    ==============================================
    1. Insert a document
    2. Insert many documents
    3. Get all documents
    4. Update a document
    5. Delete a document
    6. Exit
    ============================================== '''
    print(pattern)
    option = int(input("Enter a choice(1-6): "))
