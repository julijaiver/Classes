# Area of the circle variable. WORKING
pi = 3.14
circle_radius = float(input("Provide radius of the circle: "))
circle_area = pi * circle_radius ** 2

print(f"Area of the circle is {circle_area:.2f}")

# Rectangle area/perimeter. WORKING
rectangle_length = float(input("Provide area of the rectangle: "))
rectangle_width = float(input("Provide width of the rectangle: "))

rectangle_perimeter = rectangle_length * 2 + rectangle_width * 2
rectangle_area = rectangle_length * rectangle_width

print(f"Rectangle perimeter is {rectangle_perimeter:.2f}")
print(f"Rectangle area is {rectangle_area:.2f}")

#Medieval units. WORKING
talents = float(input("Enter talents:\n "))
pounds = float(input("Enter pounds:\n"))
lots = float(input("Enter lots:\n"))

lots_to_grams = (lots * 13.3)
pounds_to_grams = (13.3 * 32 * pounds)
talents_to_grams = (13.3 * 32 * 20 * talents)

whole_in_grams = lots_to_grams + pounds_to_grams + talents_to_grams
print(f"The weight in modern units is:\n {whole_in_grams // 1000} kg and {whole_in_grams % 1000:.3f}")

# Random numbers
import random
randomThreeDigit = random.sample(range(0, 9),3)
randomFourDigit = random.sample(range(1, 6), 4)
print(randomThreeDigit)
print(randomFourDigit)

# IF STRUCTURE
# Zander length
zanderLength = int(input("Provide zander length in centimeters: "))
if zanderLength > 42:
    print("You can keep it")
else:
    print(f"Your fish is {42 - zanderLength} centimeters too small")

# Cabin classes
cabinClass = input("Provide your cabin class: ")
cabinClass = cabinClass.upper()

if cabinClass == "LUX":
    print("upper-deck cabin with a balcony")
elif cabinClass == "A":
    print("above the car deck, equipped with a window")
elif cabinClass == "B":
    print("windowless cabin above the car deck")
elif cabinClass == "C":
    print("windowless cabin below the car deck")
else:
    print("invalid cabin class")

# Hemoglobin levels
gender = input("Provide biological gender (m/f): ")
gender = gender.lower()
hemoglobinValue = int(input("Provide hemoglobin value g/l: "))

if gender == "f" and hemoglobinValue > 155:
    print("Value too high")
elif gender == "f" and hemoglobinValue < 117:
    print("Value too low")
elif gender == "f":
    print("Value normal")
elif gender == "m" and hemoglobinValue > 167:
    print("Value too high")
elif gender == "m" and hemoglobinValue < 134:
    print("Value too low")
elif gender == "m":
    print("Value normal")

# Leap year
userInput = int(input("Enter a year: "))
if (userInput % 4 == 0) or (userInput % 100 == 0 and userInput % 400 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")

# numbers divisible by 3(two ways)
# While statement
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number +=1
# for statement
for number in range(3, 1001, 3):
    print(number)

# Inch to cm
inches = float(input("Quantity in inches: "))

while inches >= 0:
    print(f"{inches} inches is equal to {inches * 2.54:.2f} centimeters")
    inches = float(input("Quantity in inches: "))
    if inches < 0:
        print("You provided a negative value")

# GOOD EXAMPLE
# While loop and list to find highest/smallest number
numbers = []

userInput = input("Provide numbers. Use Enter to stop\n")
while userInput != "":
    try:
        number = int(userInput)
        numbers.append(number)
    except ValueError:
        print("Invalid input")
    userInput = input("Provide numbers: ")

if not numbers:
    print("No valid numbers")
else:
    min_number = min(numbers)
    max_number = max(numbers)

print("Lowest value: ", min_number, "Highest value: ", max_number)

# Without try
numberList = []

userInput = input("Provide a number: ")
while userInput != "":
    if userInput != "":
        userInput = int(userInput)
        numberList.append(userInput)
    userInput = input("Provide a number: ")

min_number = min(numberList)
max_number = max(numberList)
print("Lowest value:", min_number, "Highest value: ", max_number)

# User guessing numbers
import random
random_number = random.randint(1, 10)

userGuess = int(input("Guess the number from 1 to 10: "))
while userGuess != random_number:
    if userGuess > random_number:
        print("Too high")
    elif userGuess < random_number:
        print("Too low")
    userGuess = int(input("Guess the number from 1 to 10: "))
print("You are right")

# Checking credentials
username = "Julijaiv"
password = "1234"

inputUsername = input("Provide username: ")
inputPass = input("Provide password: ")
numberOfTries = 0
while numberOfTries < 4:
    if inputUsername != username and inputPass != password:
        print("Invalid credentials")
    else:
        print("Welcome")
        break
    numberOfTries += 1
    inputUsername = input("Provide username: ")
    inputPass = input("Provide username: ")
    if numberOfTries >= 4:
        print("Access denied")

# Dice roll
import random
diceInput = int(input("How many dice to roll? "))
sum = 0
for i in range(diceInput):
    rollDice = random.randint(1, 6)
    print(f"Dice rolled: {rollDice}")
    sum += rollDice
print(f"Sum of {diceInput} dice rolls is equal to {sum}")

# Prime numbers
inputNumber = int(input("Provide a number: "))
if inputNumber == 1:
    print("Not a prime number")
elif inputNumber > 1:
    for i in range(2, inputNumber):
        if inputNumber % i == 0:
            print("Not a prime number")
            break
        else:
            print("Prime number")

# Asking for a list and returning
cities = []
for i in range(5):
    userInput = input("Provide five cities: ")
    cities.append(userInput)
for city in cities:
    print(city)

# FunCTIONS
# Dice roll
def dice (n):
    diceNumber = random.randint(1, n)
    return diceNumber

sideNumber = int(input("What sized dice are you rolling?\n"))
while True:
    rollResult = dice(sideNumber)
    if rollResult == sideNumber:
        print(f"You got {sideNumber}")
        break
    else:
        print(f"{rollResult} rolled")

#Simple list sum
def sum_of_list(integers):
    total = sum(integers)
    return total


numbers = [12, 5, 11, 8, 13]
result = sum_of_list(numbers)
print(result)

# New list of even numbers only
def even_only(num):
    even_list = []
    for i in num:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


numbers = []

userInp = input("Provide a list of numbers. Use Enter to quit\n")
while userInp != "":
    try:
        userInp = int(userInp)
        numbers.append(userInp)
    except ValueError:
        print("Invalid value")
    userInp = input("Provide numbers: ")

print(numbers)
newList = even_only(numbers)
print(newList)

# Value for money
def unit_price(diameter, price):
    area = 3.14 * diameter**2
    sq_meters = area * 0.0001
    unit_pr = price / sq_meters
    return unit_pr


pizza1_cm = float(input("Provide diameter of 1st pizza in cm\n"))
pizza1_eur = float(input("Provide price of 1st pizza in eur\n"))
pizza2_cm = float(input("Provide diameter of 2nd pizza in cm\n"))
pizza2_eur = float(input("Provide price of 2nd pizza in eur\n"))

value_Pizza1 = unit_price(pizza1_cm, pizza1_eur)
value_Pizza2 = unit_price(pizza2_cm, pizza2_eur)

if value_Pizza1 < value_Pizza2:
    print("1st pizza provides better value for money")
elif value_Pizza1 > value_Pizza2:
    print("2nd pizza provides better value for money")
else:
    print("Input incorrect")

# Is word a palindrome
def is_palindrome(a):
    length = len(a)
    sliced = a[length::-1]
    if sliced == a:
        return True
    else:
        return False


user_word = input("Enter a string\n")
palindrome_check = is_palindrome(user_word)
if palindrome_check:
    print("Word is a palindrome")
else:
    print("Word is not a palindrome")

# Name initials
def name_initials(a, b):
    first = a[0].upper()
    last = b[0].upper()
    name = f'{first}.{last}'
    return name


name_prompt = input('First name: ')
last_name_prompt = input('Last name: ')
initials = name_initials(name_prompt, last_name_prompt)
print(f"Name initials: {initials}")

#Pillars function
def distance(pillars_nr, pillar_distance, pillar_width):
    if pillars_nr < 1:
        return "Number of pillars should be at least one"
    elif pillars_nr == 1:
        return 0
    elif pillars_nr > 1 and 10 <= pillar_distance <= 30:
        distance_between = (pillars_nr - 1) * pillar_distance + (pillars_nr - 2) * pillar_width * 0.01
        return f'Total distance between is {distance_between:.2f} meters'
    else:
        return "Invalid input"


pillar_prompt = float(input("Provide number of pillars\n"))
distance_prompt = float(input("Provide distance between pillars 10-30 (m)\n"))
width_prompt = float(input("Provide pillar width 10-50 (cm)\n"))

calculated_distance = distance(pillar_prompt, distance_prompt, width_prompt)
print(calculated_distance)

# Counting list
def count_sheeps(sheep):
    if not sheep:
        return 'List empty'
    final_result = sum(sheep)
    return final_result

# First non-consecutive number
# Long beginner way
def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[1] - arr[0] == 1:
            arr.remove(arr[0])
        elif arr[1] - arr[0] != 1:
            return arr[1]
        else:
            return None

#Clever way
def first_non_consecutive(a):
    i = a[0]
    for e in a:
        if e != i:
            return e
        i += 1
    return None


#Even or Odd
def even_or_odd(numberr):
    return 'Odd' if numberr % 2 else 'Even'

#Squaring/cubing a list
def squaring_a_list(numbers):
    square_list = []
    for i in numbers:
        square_list.append(i**2)
    return square_list


def cubing_a_list(numbers):
    cube_list = []
    for i in numbers:
        cube_list.append(i**3)
    return cube_list


numbers = list(range(1, 11))
squared_list = squaring_a_list(numbers)
cubed_list = cubing_a_list(numbers)
print(squared_list)
print(cubed_list)

#CONNECTING DICTIONARIES
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

connect = dict()

for i in range(len(keys)):
    connect.update({keys[i]: values[i]})
print(connect)

#Another way
connectt = dict(zip(keys, values))
print(connectt)

## 5l - 100km

def how_many_fuel(km):
    fuel_needed = km * 0.05
    return fuel_needed


def total_price(liters):
    price = 1.95 * liters
    return price

trip_km = []
user_km = float(input("Enter how many km you want to go: "))
needed_fuel = how_many_fuel(user_km)
trip_km.append(user_km)
print(f'You will need {needed_fuel:.2f} liters of fuel to complete the trip')

# Price = 1.95


fuel_price = total_price(how_many_fuel(user_km))
print(f"Fuel will cost you {fuel_price:.2f} euros")

# Do you want another trip?
count = 1
another_trip = input("Do you want to go to another trip? Y/N\n").upper()
while True:
    if another_trip == "N":
        print("Goodbye")
        break
    elif another_trip == "Y":
        user_km = float(input("Enter how many km you want to go: "))
        if user_km < 0:
            print("Invalid value")
        else:
            print(f'You will need {how_many_fuel(user_km):.2f} liters of fuel to complete the trip')
            print(f'Fuel will cost you {total_price(how_many_fuel(user_km)):.2f} euros')
            trip_km.append(user_km)
    else:
        print("Invalid input")
    another_trip = input("Do you want to go to another trip? Y/N\n").upper()
    count += 1

print(f"You entered your trip {count} times")
print("Your trips in km:\n")
for trip in trip_km:
    print(trip)
#Keep track of km