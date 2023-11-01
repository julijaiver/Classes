import mysql.connector
import random

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='spy_plane',
    user='root',
    password='Mariaroot6',
    autocommit=True
)

def get_airports(cont):
    sql = " select iso_country, ident, name, type, latitude_deg, longitude_deg "
    sql += " from airport where continent ='" + cont + "'"
    sql += " and not type = 'closed' group by iso_country order by rand() limit 50; "
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_goals():
    sql = "select * from goal;"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def new_game(player_name, current_airport, all_airports):
    sql = "insert into game(screen_name, location, battery_power, score) values (%s, %s , 100, 0);"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (player_name, current_airport))
    game_id = cursor.lastrowid

    # Adding goals
    goals = get_goals()
    goal_list = []
    for goal in goals:
        for i in range(0, goal['probability'], 1):
            goal_list.append(goal['id'])

    # Excluding starting airport
    game_airport = all_airports[1:].copy()
    random.shuffle(game_airport)


    for i, goal_id in enumerate(goal_list):
        sql = "insert into spying_location (game, goal, airport) values (%s, %s, %s);"
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql, (game_id, goal_id, game_airport[i]['ident']))

    return game_id

airports = get_airports("EU")
new_game("uyi", "EFHI", airports)

