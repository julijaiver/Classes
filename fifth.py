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