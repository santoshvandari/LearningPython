# Connecting to the Database
import psycopg2,datetime
connectionString = "postgresql://postgres:rnR0uiDqNVWiBL1C@db.xirdbhvrdyarslorlufu.supabase.co:5432/postgres"
try:
    connection = psycopg2.connect(connectionString)
    cursor = connection.cursor()
    # cursor.execute('truncate ipodetails;')
    print("Connected to PostgreSQL database successfully!")
except Exception as e:
    print(f"Error connecting to database: {e}")
    exit(1)


# for reading the data according to the opening date of the IPO
# Reading the Data from the Database
date = datetime.datetime.now().date()
print(date)
query=f"select * from ipodetails where openingdate='{date}';"
print(query)
cursor.execute(query)
result = cursor.fetchall()
print(result)
if result:
    for row in result:
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
connection.commit()




# for Reading the data according to the closing date fo the ipo 
# Reading the Data from the Database
date = datetime.datetime.now().date()
print(date)
query=f"select * from ipodetails where closingdate='{date}';"
print(query)
cursor.execute(query)
result = cursor.fetchall()
print(result)
if result:
    for row in result:
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
connection.commit()