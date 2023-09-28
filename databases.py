import mysql.connector

# First exercise
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

#Second exercise
def get_country_airports(area_code):
    sql = "select type, count(*) from airport, country where country.iso_country = airport.iso_country "
    sql += "and country.iso_country = '" + area_code + "'group by type order by count(*) desc;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        print(f"Airports in {area_code}:")
        for row in result:
            print(f"{row[0]}: {row[1]}")
    return


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Mariaroot6',
    autocommit=True
)


area = input("Enter area code: ").upper()
get_country_airports(area)


