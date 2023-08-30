x = int(input("How much cash might you have? "))
string = "You have {} cash"
print(string.format(x))
print(f"You said that you have {x}")

x = int(input("How much cash do you have? "))
asw = input("Can I look into your wallet? (y/n) ")
if x >= 1000 and asw == 'y':
    print("You're rich")
elif x > 10:
    print("You have more that 10 euros")
else:
    print("You're poor")

# First exercise

zanderLength = int(input("Zander length in centimeters: "))

if zanderLength < 42:
    print(f"Your fish is {42 - zanderLength} centimeters too small. Release the fish")

# Second exercise

cabinClass = input("Enter cabin class: ")
cabinClass = cabinClass.upper()

if cabinClass == 'LUX':
    print("Upper-deck cabin with a balcony")
elif cabinClass == 'A':
    print("Windowless cabin above the car deck")
elif cabinClass == 'B':
    print("Windowless cabin above the car deck")
elif cabinClass == 'C':
    print("Windowless cabin below the car deck")
else:
    print("Invalid cabin class")

# Third exercise

gender = input("Provide biological gender (m/f): ")
hemoglobinValue = int(input("Provide hemoglobin value g/l: "))

if gender == 'f' and hemoglobinValue < 117:
    print("Your hemoglobin level is too low")
elif gender == 'f' and hemoglobinValue > 155:
    print("Your hemoglobin level is too high")
elif gender == 'f':
    print("Hemoglobin level is normal")
elif gender == 'm' and hemoglobinValue < 134:
    print("Your hemoglobin level is too low")
elif gender == 'm' and hemoglobinValue > 167:
    print("Your hemoglobin level is too high")
elif gender == 'm':
    print("Hemoglobin level is normal")












