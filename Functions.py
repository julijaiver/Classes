import random
# First exercise
def dice ():
    diceNumber = random.randint(1, 6)
    return diceNumber


while True:
    rollResult = dice()
    if rollResult == 6:
        print("You got 6")
        break
    else:
        print(f"{rollResult} rolled")

# Second exercise
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
