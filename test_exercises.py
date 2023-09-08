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