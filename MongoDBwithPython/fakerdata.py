from faker import Faker
from dbconnection import get_db_connection

db= get_db_connection()

fake = Faker()

for i in range (10000000000000000000000):
    name=fake.name()
    age=fake.random_int(min=18, max=100, step=1)
    email=fake.email()
    data = {
        "name": name,
        "age": age,
        "email": email
    }
    db.user.insert_one(data)
    print(f"Data inserted with id: {data}")
