# First exercise

number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1

# Second exercise

inches = int(input("Input quantity in inches: "))
while inches > 0:
    print(f"{inches} inches is equal to {inches * 2.54 :.2f} centimeters")
    inches = int(input("Input quantity in inches: "))
    if inches <= 0:
        print("Program ended.")

# Third exercise (need help)

numberInput = input("Enter your numbers: ")
while numberInput != "":
    if numberInput == "":
        break
    numberInput = input("Enter your numbers: ")

smallest = min(numberInput)
largest = max(numberInput)
print(f"The smallest number is: {smallest}")
print(f"The largest number is: {largest}")

# Tried fixing with lists
# Wit if statement
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
numbers = []

# With 'try'
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

# Fourth exercise

import random

randomNumber = random.randint(1, 10)

while True:
    userGuess = int(input("Guess the number from 1 to 10: "))
    if userGuess == randomNumber:
        print("You guessed correct")
        break
    elif userGuess < randomNumber:
        print("Too low")
    else:
        print("Too high")
# Another way worked
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

# Fifth exercise

username = "Julija"
password = "ivaske"
attempt = 0

while attempt < 5:
    usernameInput = input("Enter username: ")
    passwordInput = input("Enter password: ")

    if usernameInput == username and passwordInput == password:
        print("Welcome")
        break
    else:
        print("Enter username and password again")
        attempt += 1

if attempt >= 5:
    print("Access denied")