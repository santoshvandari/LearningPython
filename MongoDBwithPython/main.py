from dbconnection import get_db_connection

db=get_db_connection()

def get_all_documents():
    userinfo=db.user.find()
    print("All documents in user collection")
    for user in userinfo:
        print(user)

def insert_document():
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        email = input("Enter email: ")
        data = {
            "name": name,
            "age": age,
            "email": email
        }
    except Exception as e:
        print("Invalid input")
        return

    res=db.user.insert_one(data)
    print(f"Document inserted with id: {res.inserted_id}")


def main():
    pattern = '''==============================================
    1. Insert a document
    2. Get all documents
    3. Update a document
    4. Delete a document
    5. Exit
    ============================================== '''
    print(pattern)
    option = int(input("Enter a choice(1-5): "))

    match option:
        case 1:
            insert_document()
        case 2:
            get_all_documents()
        case 5:
            print("Exiting...")
            exit(0)
        case _:
            print("Invalid choice")
            main()
    main()




if __name__=="__main__":
    print('''==============================================
    Welcome to MongoDB CRUD operations
    ============================================== ''')
    main()
    
