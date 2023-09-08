# First exercise

import random
diceTimes = int(input("How many dice to roll?\n"))
sum = 0

for i in range(diceTimes):
    diceRoll = random.randint(1, 6)
    sum += diceRoll

print(f"Total sum of {diceTimes} dice rolled is {sum}")

