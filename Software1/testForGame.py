import mysql.connector
import random
from geopy import distance



connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='spy_plane',
    user='root',
    password='Mariaroot6',
    autocommit=True
)


def get_airport_info(icao):
    sql = " select country.name, ident, airport.name, latitude_deg, longitude_deg from airport, country "
    sql += " where airport.iso_country = country.iso_country and ident = '" + icao + "'"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchone()
    return result
print(get_airport_info("EFHK"))


def airport_distance(starting, end):
    start = get_airport_info(starting)
    ending = get_airport_info(end)
    start_coordinates = (start['latitude_deg'], start['longitude_deg'])
    end_coordinates = (ending['latitude_deg'], ending['longitude_deg'])

    return int(distance.distance(start_coordinates, end_coordinates).km)

print(airport_distance('ESCF', 'EFAA'))


def airports_in_range(icao, airports, remaining_battery):
    in_range = []
    for airport in airports:
        distance = airport_distance(icao, airport['ident'])
        if (distance <= remaining_battery and not distance == 0):
            in_range.append(airport)
    return in_range

def get_airports(cont):
    sql = " select iso_country, ident, name, type, latitude_deg, longitude_deg "
    sql += " from airport where continent ='" + cont + "'"
    sql += " and not type = 'closed' group by iso_country order by rand() limit 50; "
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

airports = get_airports("EU")

print(airports_in_range('EFAA', airports, 42000))

