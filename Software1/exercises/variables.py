# Calculation of circle area
pi = 3.14159265
formatPi = f"value of Pi: {pi:.2f}"
print(formatPi)

radius = float(input("Enter the radius: "))
areaCircle = pi * radius**2
print(f"Area of circle: {areaCircle:.2f}")

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
numberAverage = f"{(numberSum / 3):.3f}"

print(numberSum)
print(numberProduct)
print(numberAverage)

# Medieval unit conversion
talents = float(input("Enter talents:\n "))
pounds = float(input("Enter pounds:\n"))
lots = float(input("Enter lots:\n"))

lots_to_grams = (lots * 13.3)
pounds_to_grams = (13.3 * 32 * pounds)
talents_to_grams = (13.3 * 32 * 20 * talents)

whole_in_grams = lots_to_grams + pounds_to_grams + talents_to_grams
print(f"The weight in modern units is:\n {whole_in_grams // 1000} kg and {whole_in_grams % 1000:.3f}")


# Random number combinations
import random
randomThreeDigit = random.sample(range(0, 9),3)
randomFourDigit = random.sample(range(1, 6), 4)
print(randomThreeDigit)
print(randomFourDigit)

