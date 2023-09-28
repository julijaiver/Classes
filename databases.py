import mysql.connector


def get_airport(ICAO):
    sql = "select airport.name, municipality from airport where ident ='" + ICAO + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Airport name: {row[0]}\n Airport located in: {row[1]}")
    return


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Mariaroot6',
    autocommit=True
)

ICAO = input("Enter ICAO code for the airport: ").upper()
get_airport(ICAO)