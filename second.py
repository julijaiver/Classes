# Calculation of circle area
pi = 3.14159265
formatPi = f"value of Pi: {pi:.2f}"
print(formatPi)

radius = float(input("Enter the radius: "))
areaCircle = pi * radius**2
print (f"Area of circle: {areaCircle:.2f}")

# Perimeter calculation
rectangleLength = float(input("Rectangle length: "))
rectangleWidth = int(input("Rectangle width: "))
rectanglePerimeter = rectangleLength*2 + rectangleWidth*2
print("Rectangle perimeter is: ", rectanglePerimeter)

# Integer sum, product and average
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
num3 = float(input("Third number: "))
numberSum = num1 + num2 + num3
numberProduct = num1 * num2 * num3
numberAverage = float(numberSum / 3)

print(numberSum)
print(numberProduct)
print(numberAverage)

import random
randomNumber = random.randint(0, 9)
print(randomNumber)

