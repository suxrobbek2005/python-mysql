import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Djcoder1120'
)

if connection.is_connected():
    print("mysql ga muvaffaqiyatli ulandik.")
