from flask import Flask, jsonify
import mysql.connector

# Exercise 1
app = Flask(__name__)

def is_prime_number(number):
    number = int(number)
    if number == 1:
        return False
    elif number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
    return True


@app.route('/prime_number/<int:number>')
def check_prime_number(number):
    is_prime = is_prime_number(number)
    response = {
        "Number": number,
        "isPrime": is_prime
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)


# Exercise 2
app = Flask(__name__)

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='pass',
    autocommit=True
)

def get_airport(ICAO):
    sql = "select airport.name, municipality from airport where ident ='" + ICAO + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            name = row[0]
            location = row[1]
    return name, location

@app.route('/airport/<ICAO>')
def airport_response(ICAO):
    name, location = get_airport(ICAO)
    response = {
        "ICAO": ICAO,
        "Name": name,
        "Location": location
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(use_reloader=True, host = '127.0.0.1', port=5000)

