# WHILE loops

uInput = ''
while uInput != 'stop':
    uInput = input("Give a command (use 'stop' to stop): ")
    if uInput == 'delete':
        print("Oh my, not the delete command..")
        break
    print(f"You gave {uinput} command")

print("This is the end")

# Nested while loops

a = 0

while a < 5:
    b = 0
    while b < 6:
        b += 1
        print(f"{a} multiplied with {b} is {a*b}")
    a += 1

# LIST structures

lst = ["Kimmo", "Mohammad", "Jane"]

print(lst[0])
print(lst[-2])
# To print range (not including the last one)
print(lst[0:2])
# From 1 til the end
print(lst[1:])

# FOR loops

lst = ["Kimmo", "Mohammad", "Jane", "Kalle"]

for x in lst:
    print(f"x is {x}")
    if x == "Jane":
        break

lst = ["Kimmo", "Janne", "Mohammad", "Jane"]

for xid, x in enumerate(lst):
    if x != lst[-1]:
        print(f"{x} is having coffee with {lst[xid +1]}")
    #print(f"x is {x} and the lst index is {xid}")

# 0 to 6, every 2 numbers
for i in range(0, 6, 2):
    print(i)

for i in range(10, -1, -1):
    print(i)

str = "dfguyhio"
for i in range(0, len(str), 2):
    print(str[i])

# Parts of integers
nm = 545.4582
print(f"Integer part is {int(nm)} and the fraction part is {nm%1}")

lst = ["Kimmo", "Janne", "Mohammad", "Jane"]

newList = [x for x in lst if x != "Kimmo"]
print(f"New list is {newList}")

# Changing strings in list to numbers
nmb = ["23", "4", "56"]
nmb = [int(x) for x in nmb]
print(nmb)

#FUNCTIONS

def greet():
    print("Hello")

def greeting(n):
    for i in range(n):
        greet()

def sum (a, b):
    total = a+b
    return total

num1 = int(input("Provide the first number: "))
num2 = int(input("Provide the second number: "))

print("Sum: ", sum(num1, num2))

# calculator. Build a simple calculator to sum, subtract, multiply, division of three given numbers

def number_sum(a, b):
    total = a + b
    return total

def number_subtract(a, b):
    total = a - b
    return total

def multiplication(a, b):
    total = a*b
    return total

def division(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    total = a/b
    return total

num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))

print(f"Sum: {number_sum(num1, num2)}, Subtraction: {number_subtract(num1, num2)}")
print(f"Product: {multiplication(num1, num2)}, Division: {division(num1, num2)}")

# Exercise shop.list NOT how it should be
shoppingList = []

userInput = int(input("Choose an operation:\n1 - Add to the list\n2 - Remove from the list\n"
                      "3 - Show the last item in the list\n4 - Quit\n"))
while userInput != 4:
    if userInput == 1:
        newItem = input("Enter item: ")
        shoppingList.append(newItem)
    elif userInput == 2:
        if not shoppingList:
            print("Shopping list empty")
        else:
            del shoppingList[-1]
    elif userInput == 3:
        printList = shoppingList[-1]
        print(printList)
    userInput = int(input("Enter a command: "))

print("This is the final shopping list:", shoppingList)
print("Goodbye")

# Tuples
patient = "Laura", "Jones", "29", "Flu"
print(patient)

def format_patient_info(patient_info):
    first_name, last_name, age, symptoms = patient_info
    formatted_info = print(f"Name: {first_name} {last_name}, Age: {age}, Symptoms: {symptoms}")
    return formatted_info

format_patient_info(patient)

#Scores to grades function
scores = [46, 92, 39, 67, 82, 99, 94]


def classify_grades(a):
    if a >= 90:
        return "A"
    elif 80 <= a <= 89:
        return "B"
    elif 70 <= a <= 79:
        return "C"
    elif 60 <= a <= 69:
        return "D"
    elif a <= 60:
        return "F"


for score in scores:
    grade = classify_grades(score)
    print(f"The final grade is {grade}")

avg_score = sum(scores)/len(scores)
print(f"Average score is {avg_score:.2f}")

# Classify temperatures
temperatures = [25, 10, -5, 30, 18, 5, 35, 22]

for temp in temperatures:
    if temp < 0:
        category = "Freezing"
    elif temp <= 10:
        category = "Cold"
    elif temp <= 20:
        category = "Moderate"
    elif temp <= 30:
        category = "Warm"
    else:
        category = "Hot"
    print(f"Temperature: {temp}°C, Category: {category}")

# Shopping list with function not perfect
def add_task(a, b):
    a.append(b)


def remove_task(a, b):
    if b in a:
        a.remove(b)
    else:
        print("Item not found")


def display_task(a):
    for item in a:
        print(item)


shopping_list = []

while True:
    user_operation = input("Enter a command\n")
    if user_operation == "4":
        print("Program quit")
        break
    elif user_operation == "1":
        user_add = input("Add a task\n")
        user_add = user_add.lower()
        add_task(shopping_list, user_add)
    elif user_operation == "2":
        user_remove = input("Remove a task\n")
        user_remove = user_remove.lower()
        remove_task(shopping_list, user_remove)
    elif user_operation == "3":
        print("Here is your list:\n")
        display_task(shopping_list)
    user_list = input("Enter a command\n")

#Shopping list again
shopping_list = []
user_prompt = input("1-Add to the list\n2-Remove from the list\n3-Display list\n4-Quit\nSelect command: ")

while user_prompt != '4':
    if user_prompt == '1':
        adding = input('Add to the list: ')
        adding = adding.lower()
        shopping_list.append(adding)
    elif user_prompt == '2':
        if not shopping_list:
            print('List empty')
        else:
            removing = input("Remove item: ")
            if removing in shopping_list:
                shopping_list.remove(removing)
            else:
                print('Not found')
    elif user_prompt == '3':
        if not shopping_list:
            print('List empty')
        for index, item in enumerate(shopping_list, start = 1):
            print(f"{index}.{item}")
    user_prompt = input('Select command: ')
print('Program ended. Final shopping list:\n')
for index, item in enumerate(shopping_list, start=1):
    print(f"{index}.{item}")
