# First exercise
seasons = ("Spring", "Summer", "Autumn", "Winter")
userInput = int(input("Which month is it 1-12?\n"))
if 1 <= userInput <= 3:
    print(f"Month number {userInput} is in {seasons[3]}")
elif 4 <= userInput <= 6:
    print(f"Month number {userInput} is in {seasons[0]}")
elif 7 <= userInput <= 9:
    print(f"Month number {userInput} is in {seasons[1]}")
elif 10 <= userInput <= 12:
    print(f"Month number {userInput} is in {seasons[2]}")
else:
    print("Invalid input")

# Second exercise
names = set()
users_names = input("Provide names. Use Enter to quit\n")
while users_names != "":
    if users_names in names:
        print("Existing name")
    else:
        print("New name")
    names.add(users_names)
    users_names = input("Provide a name\n")
for name in names:
    print(name)

#Third exercise
airport_codes = {"EFHK": "Helsinki-Vantaa Airport",
                 "EDDC": "Dresden Airport",
                 "EGSS": "London Stansted Airport"}

user_input = input("1 - Enter a new airport\n2 - Find an airport\n3 - Quit\n")
while user_input != "3":
    if user_input == "1":
        code = input("Enter ICAO code:\n")
        code = code.upper()
        name = input("Enter name of the airport:\n")
        name = name.title()
        if code in airport_codes:
            print("Airport already exists")
        else:
            airport_codes[code] = name
            print("Aiport added")
    if user_input == "2":
        find_code = input("Enter ICAO code:\n")
        find_code = find_code.upper()
        if find_code in airport_codes:
            print(airport_codes[find_code])
        else:
            print("Not found")
    user_input = input("Select operation\n")