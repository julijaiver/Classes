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

# Third exercise
def gallon_to_litre(n):
    result = n * 3.785
    return result


gasolineQuantity = float(input("How much gallons of gasoline? "))
litres = gallon_to_litre(gasolineQuantity)
while gasolineQuantity >= 0:
    print(f"{gasolineQuantity} gallons is {litres:.3f} litres")
    break
if gasolineQuantity < 0:
    print("You entered a negative number")

# Fourth exercise
def sum_of_list(a):
    total = sum(a)
    return total


numbers = [12, 5, 11, 8, 13]
result = sum_of_list(numbers)
print(result)

# Fifth exercise (with user input)
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

# Sixth exercise
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