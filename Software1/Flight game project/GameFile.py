import random
from geopy import distance
import mysql.connector
import spyPlaneStory

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='spy_plane',
    user='root',
    password='Mariaroot6',
    autocommit=True
)


# fetch airports from different continents
def get_airports(cont):
    sql = " select iso_country, ident, name, type, latitude_deg, longitude_deg "
    sql += " from airport where continent ='" + cont + "'"
    sql += " and not type = 'closed' group by iso_country order by rand() limit 50; "
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


# new game
def new_game(player_name, current_airport, all_airports):
    sql = "insert into game(screen_name, location, battery_power, score) values (%s, %s , 6000, 0);"
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
        if i < len(game_airport):
            sql = "insert into spying_location (game, goal, airport) values (%s, %s, %s);"
            cursor = connection.cursor(dictionary=True)
            cursor.execute(sql, (game_id, goal_id, game_airport[i]['ident']))

    return game_id


# Get airport information
def get_airport_info(icao):
    sql = " select country.name, ident, airport.name, latitude_deg, longitude_deg from airport, country "
    sql += " where airport.iso_country = country.iso_country and ident = '" + icao + "'"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


# Set airport as visited
def airport_visited(game, airport):
    sql = f"update spying_location set visited = 1 where game = %s and airport = %s;"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (game, airport))

# Check if airport is visited
def is_visited(game, airport):
    sql = f"select visited from spying_location where game = %s and airport = %s"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (game, airport))
    result = cursor.fetchone()

    if result == ({'visited': 1}):
        return False
    else:
        return True

# What goal is in the location
def location_goal(game_id, location):
    sql = (f"select spying_location.id, goal, goal.id as goal, name, points from spying_location "
           f"inner join goal on goal.id = spying_location.goal where game = %s and airport = %s; ")
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (game_id, location))
    result = cursor.fetchone()
    return result


# Distance between airports
def airport_distance(starting, end):
    start = get_airport_info(starting)
    ending = get_airport_info(end)
    start_coordinates = (start[0]['latitude_deg'], start[0]['longitude_deg'])
    end_coordinates = (ending[0]['latitude_deg'], ending[0]['longitude_deg'])

    return int(distance.distance(start_coordinates, end_coordinates).km)


# get airports in range:
def airports_in_range(icao, airports, remaining_battery,game_id):
    in_range = []
    for i, airport in enumerate(airports):
        if(i>=1):
            distance = airport_distance(icao, airport['ident'])
            sql = (f"SELECT visited FROM spying_location WHERE game = %s AND airport = %s;")
            cursor = connection.cursor()
            cursor.execute(sql,(game_id,airport['ident']))
            airport_visited = cursor.fetchone()
            if (distance <= remaining_battery and not distance == 0 and not airport_visited[0] == 1):
                in_range.append(airport)
    return in_range


# update location
def location_update(icao, bat_power, score, id):
    sql = f"update game set location = %s, battery_power = %s, score = %s where id = %s;"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (icao, bat_power, score, id))


# Formulate messages in the main
def path_game_won(path_choice):
    rand_path = random.randint(1, 5)
    if int(path_choice) == rand_path:
        return False
    else:
        return True


# Y or N for the minigame
def yes_or_no(question: str) -> bool:
    while True:
        answer = input(question).upper()
        if answer in ("Y", "N"):
            return answer == "Y"
        print("Invalid input.")


# Retrieve the data of top 10 players in the game
def get_rank():
    sql = ("SELECT id,screen_name,score FROM game WHERE score >=100 ORDER BY score DESC limit 10;")
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


storyDialog = input('Do you want to read the background story? Y/N: ').upper()
if storyDialog == 'Y':
    for line in spyPlaneStory.getStory():
        print(line)

# GAME SETTINGS
print("\nWhen you are ready to start, ")
player = input("type your name: ")
# boolean for game over and win
game_over = False
win = False

# start battery = 6000
battery = 6000

# start score = 0
score = 0

# all airports & level selection
print("Select your continent, "
      "\nEU - Europe (Easy)"
      "\nAF - Africa (Medium)"
      "\nAS - Asia (Hard)")
while True:
    continent = input("EU/AF/AS : ").upper()
    if continent == "AS" or continent == "AF" or continent == "EU":
        break
    else:
        print("Please enter AS/AF/EU")
all_airports = get_airports(continent)

# start_airport ident
start_airport = all_airports[0]['ident']

# current airport
current_airport = start_airport

# game id
game_id = new_game(player, current_airport, all_airports)

# sets start airport as visited
airport_visited(game_id, current_airport)

# GAME LOOP
while not game_over:
    # get current airport info
    airport = get_airport_info(current_airport)
    # fetch game status
    print(f"You are at {airport[0]['name']}.")
    print(f"You have {battery}km of range in your battery.")
    # pause
    input("\nPress Enter to continue.")

    # goal stuff
    goal = location_goal(game_id, current_airport)
    if goal:
        if goal['goal'] == 1:
            print("The airport is clear and sunny. You gain 5 points.")
            score = score + 5
        elif goal['goal'] == 2:
            if battery - 50 < 0:
                print(
                    f"Oh no, the weather in {airport[0]['name']} looks bad. "
                    f"Your remaining battery range cannot get you there. You have to do an emergency landing.")
                battery = 0
                game_over = True
                break
            else:
                print(
                    f"The weather in {airport[0]['name']} is Cloudy. You get 10 points,but you spend 50km extra range.")
                battery = battery - 50
                score = score + 10
        elif goal['goal'] == 3:
            user_choice = yes_or_no("There is a charging point nearby, but this airport seems to be suspicious. "
                                    "\nWould you like to take the risk,"
                                    "\nchoose a path and try to get to the charging point? "
                                    "\nIf not, then the only way forward is to leave and"
                                    "\nyou will not be able to come back to this airport again."
                                    "\nChoose if you want to take the risk Y/N: ")
            if user_choice:
                path_choice = input('Choose a path 1 - 5: ')
                while not (path_choice.isdigit() and 1 <= int(path_choice) <= 5):
                    path_choice = input('Please enter a path # from 1 to 5: ')
                if path_game_won(path_choice):
                    print("Your path was successful! You got 600 extra battery power and 15 points")
                    battery += 600
                    score += 15
                    print(f"You now have {battery} km of range in your battery.")
                else:
                    game_over = True
                    break
            else:
                print("You did not take the risk, but lost the resources used to travel")
        else:
            print("This airport was expecting you. You have been caught!")
            game_over = True
            break
        input("\nPress Enter to continue.")

    # if no battery power, game over
    # show airports in range. if none, game over
    airports = airports_in_range(current_airport, all_airports, battery,game_id)
    print(f"\nThere are {len(airports)} airports in range: ")
    if len(airports) == 0:
        print("You have no more airports in range.")
        game_over = True
    else:
        print("Airports:")
        for airport in airports:
            if is_visited(game_id, airport['ident']):
                ap_distance = airport_distance(current_airport, airport['ident'])
                print(f"{airport['name']}, icao: {airport['ident']}, distance: {ap_distance:.0f}km")

        # ask for destination
        while True:
            airport_codes = [dict['ident'] for dict in airports]
            dest = input("\nEnter the ICAO of the destination you would like to go to: ").upper()
            if dest in airport_codes:
                break
            else:
                print("Please enter a correct ICAO.")
        selected_distance = airport_distance(current_airport, dest)
        battery -= selected_distance
        location_update(dest, battery, score, game_id)
        current_airport = dest
        airport_visited(game_id, current_airport)
        if battery < 0:
            game_over = True

if score >= 100:
    win = True

# if game is over the loop stops
if win:
    print(f"You won! You have gathered {score} points worth of information")
    win_lists = get_rank()
    for win_list in win_lists:
        if game_id == win_list['id']:
            print(f"Congratulations, you are in the top 10 rank and you rank as No.{win_lists.index(win_list)+1} in the list.")
else:
    print(f"You lose, you have gathered {score} points worth of information. This is not enough!")