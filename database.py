# print("hello")
import pymysql

def connect_to_db():
    return pymysql.connect(
        host="localhost",
        user="testabs",
        password="need2know!",
        database="test_asbestos"
    )

def fetch_data(query):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result


query = "SELECT id, caseNumber, status, businessName FROM cases limit 5 order by id desc"
raw_data = fetch_data(query)

print(raw_data)