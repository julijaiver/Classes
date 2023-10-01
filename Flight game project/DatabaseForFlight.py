import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='spy_plane',
    user='root',
    password='Mariaroot6',
    autocommit=True
)


# fetch airports from different continents
def get_eu_airports():
    sql = """select iso_country, ident, name, type, latitude_deg, longitude_deg
from airport 
where iso_country in(select iso_country from airport where continent = "EU")
and ident in(select min(ident) from airport where continent = "EU" 
and type = "large_airport" or type = "small_airport" group by iso_country)
order by rand()
limit 40;"""
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def get_africa_airports():
    sql = """select iso_country, ident, name, type, latitude_deg, longitude_deg
    from airport 
    where iso_country in(select iso_country from airport where continent = "AF")
    and ident in(select min(ident) from airport where continent = "AF" 
    and not type = "closed" group by iso_country)
    order by rand()
    limit 40;"""
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def get_asia_airports():
    sql = """select iso_country, ident, name, type, latitude_deg, longitude_deg
    from airport 
    where iso_country in(select iso_country from airport where continent = "AS")
    and ident in(select min(ident) from airport where continent = "AS" 
    and not type = "closed" group by iso_country)
    order by rand()
    limit 40;"""
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def get_north_am_airports():
    sql = """select iso_country, ident, name, type, latitude_deg, longitude_deg
    from airport 
    where iso_country in(select iso_country from airport where continent = "NA")
    and ident in(select min(ident) from airport where continent = "NA" 
    and not type = "closed" group by iso_country)
    order by rand()
    limit 40;"""
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


# fetch goals
def get_goals():
    sql = "select * from goal;"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def new_game(player_name, current_airport, battery_power, all_airports):
    sql = "insert into game(screen_name, location, battery_power, score) values (%s, %s, %s, %s);"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (player_name, current_airport, battery_power))

    #Maybe adding goals
    goals = get_goals()
    goal_list = []
    for goal in goals:
        for i in range(0, goal['probability'], 1):
            goal_list.append(goal['id']



