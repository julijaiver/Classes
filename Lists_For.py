# First exercise

import random
diceTimes = int(input("How many dice to roll?\n"))
sum = 0

for i in range(diceTimes):
    diceRoll = random.randint(1, 6)
    sum += diceRoll

print(f"Total sum of {diceTimes} dice rolled is {sum}")

# Second exercise

numbers = []
inputNumbers = input("Enter numbers (press 'Enter' to stop): ")
while inputNumbers != "":
    numbers.append(inputNumbers)
    inputNumbers = input("Enter numbers (press 'Enter' to stop): ")

numbers = [int(x) for x in numbers]
numbers.sort(reverse=True)
for i in range(5):
    print(numbers[i])

# Third exercise

inpNumber = int(input("Provide a number: "))
if inpNumber == 1:
    print("Not a prime number")
elif inpNumber > 1:
    for i in range(2, inpNumber):
        if inpNumber % i == 0:
            print(f"{inpNumber} is a not prime number")
            break
    else:
        print(f"{inpNumber} is a prime number")


# Fourth testing

cities = []
inputInt = input("Provide five names of cities: ")

for i in range(5):
    cities.append(inputInt)
    inputInt = input("Provide names of cities: ")

for city in cities:
    print(city)





