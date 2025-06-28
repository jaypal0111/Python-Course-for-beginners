# print("hello")
import pymysql

def connect_to_db():
    return pymysql.connect(
        host="localhost",
        user="jay",
        port= 8889,
        password="home1234",
        database="test_asbestos"
    )

# db = connect_to_db()

# print(db)

def fetch_data(query):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result


query = "SELECT id, caseNumber, status, businessName FROM cases order by id desc limit 5"
raw_data = fetch_data(query)

print(raw_data)