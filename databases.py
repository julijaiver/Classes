import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='duckburg',
    user='root',
    password='Mariaroot6',
    autocommit=True
)

sql = "select * from duckburger"
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()
if cursor.rowcount > 0:
    for row in result:
        print(row)
