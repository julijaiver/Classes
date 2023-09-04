prompt = "\nTell me something and I will repeat it for you"
prompt += "\nEnter 'quit' to exit the program\n"
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

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
