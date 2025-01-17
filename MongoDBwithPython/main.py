from dbconnection import get_db_connection
from bson import ObjectId

db=get_db_connection()

def get_all_documents():
    userinfo=db.user.find()
    print("All Data in user collection")
    for user in userinfo:
        print(user)

def insert_document():
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        email = input("Enter email: ")
        if not name or not age or not email:
            print("Invalid input")
            insert_document()
        data = {
            "name": name,
            "age": age,
            "email": email
        }
    except Exception as e:
        print("Invalid input")
        return

    res=db.user.insert_one(data)
    print(f"Data inserted with id: {res.inserted_id}")
    return

def update_document():
    try:
        id=input("Enter the id of the data to update: ")
        if not ObjectId.is_valid(id):
            print("Invalid id")
            return
        id = ObjectId(id)
        userinfo=db.user.find_one({"_id":id})
        if userinfo:
            print(f"Data found with id: {id}. Enter new data and Press Enter for no change")
            name = input("Enter name: ")
            age = input("Enter age: ")
            email = input("Enter email: ")
            if age:
                age = int(age)
            if not name and not age and not email:
                print("No data entered. Exiting...")
                return
            data = {
                "name": name if name else userinfo["name"],
                "age": age if age else userinfo["age"],
                "email": email if email else userinfo["email"]
            }
        else:
            print("Data not found")
            return
    except Exception as e:
        print("Invalid input")
        return

    res=db.user.update_one({"_id":id},{"$set":data})
    print(f"Data updated with id: {res.upserted_id}")
    return


def delete_document():
    try:
        id=input("Enter the id of the data to delete: ")
        if not ObjectId.is_valid(id):
            print("Invalid id")
            return
        id = ObjectId(id)
        userinfo=db.user.find_one({"_id":id})
        if userinfo:
            print(f"Data found with id: {id}.\nDo you want to delete? (y/n)",end=" : ")
            choice = input()
            if choice.lower()=="y":
                res=db.user.delete_one({"_id":id})
                print(f"Data deleted Successfully")
            else:
                print("Data not deleted")
        else:
            print("Data not found")
            return
    except Exception as e:
        print("Invalid input")
        return


def main():
    pattern = '''
==============================================
    1. Insert a Data
    2. Get all Data
    3. Update a Data
    4. Delete a Data
    5. Exit
============================================== '''
    print(pattern)
    option = int(input("Enter a choice(1-5): "))

    match option:
        case 1:
            insert_document()
        case 2:
            get_all_documents()
        case 3:
            update_document()
        case 4:
            delete_document()
        case 5:
            print("Exiting...")
            exit(0)
        case _:
            print("Invalid choice")
    main()




if __name__=="__main__":
    print('''==============================================
    Welcome to MongoDB CRUD operations
============================================== ''')
    main()
    
