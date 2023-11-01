class Item:
    def __init__(self, name, price, quantity=0):
        # Run validations to received arguments
        assert price >= 0, f"Price {price} is not greater than zero"
        assert quantity >= 0
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity


item1 = Item("Phone", 100)
item2 = Item("Laptop", 1420, 2)

# Amir's exercise
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def display_courses(self):
        return [course.name for course in self.courses]


class Course:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.students = []

    def add_students(self, student):
        self.students.append(student)

    def display_students(self):
        return [student.name for student in self.students]


student1 = Student(1, "Timo")
student2 = Student(2, "Anna")
student3 = Student(3, "Tung")

course1 = Course(101, "Mathematics")
course2 = Course(102, "English")
course3 = Course(105, "Physics")

student1.enroll(course3)
student1.enroll(course2)

print("Students enrolled in the Physics course:")
print(f"{course3.name} has {course3.display_students()}")

# Python crash course Restaurant
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.name}\nRestaurant type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant {self.name} is now open")

    def set_served_per_day(self, customers):
        self.number_served += customers


restaurant1 = Restaurant("Lucky duck", "Chinese")
restaurant2 = Restaurant("Bom spaghetti", "Italian")
restaurant3 = Restaurant("Grill chill", "Grill")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# Crash course User

class User:
    def __init__(self, first_name, last_name, birth_date, date_joined):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.date_joined = date_joined
        self.login_attempts = 0

    def describe_user(self):
        print(f"User name: {self.first_name} {self.last_name}\nDate of birth: {self.birth_date}\n"
              f"Date joined: {self.date_joined}")

    def greet_user(self):
        print(f"Welcome, {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Julija", "Ivaskeviciute", "02.03.1997", "10.25.2023")
user2 = User("Saggad", "Farhan", "11.05.99", "07.10.2023")
user1.describe_user()
user2.describe_user()

user1.greet_user()
user2.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

# ChatG Address and Person
class Address:
    def __init__(self, street, city, postal_code):
        self.street = street
        self.city = city
        self.postal_code = postal_code

    def display_address(self):
        print(f"Address: {self.street}, {self.city}, {self.postal_code}")


class Person:
    def __init__(self, name, age, street, city, postal_code):
        self.name = name
        self.age = age
        self.address = Address(street, city, postal_code)

    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")
        self.address.display_address()


person = Person("Julija", 27, "Lehtovuorenkatu", "Helsinki", "00390")
person.display_info()

# ChatG Library
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book(self):
        print(f"Title: {self.title}, Author: {self.author}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def display_books(self):
        for book in self.books:
            book.display_book()


library = Library()
library.add_book("1984", "George Orwell")
library.add_book("Harry Potter", "J.K.Rowling")
library.display_books()

# ChatG computer composition
class CPU:
    def __init__(self, speed):
        self.speed = speed

class RAM:
    def __init__(self, size):
        self.size = size

class HardDrive:
    def __init__(self, capacity):
        self.capacity = capacity

class Computer:
    def __init__(self, cpu_speed, ram_size, drive_capacity):
        self.speed = CPU(cpu_speed)
        self.size = RAM(ram_size)
        self.capacity = HardDrive(drive_capacity)

    def display_specifications(self):
        print(f"Specifications:\nCPU speed: {self.speed.speed}, RAM size: {self.size.size}, "
              f"Hard drive capacity: {self.capacity.capacity}")


new_computer = Computer(100, 16, "1Tb")
new_computer.display_specifications()

# ChatG music library
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def display_song(self):
        print(f"Title: {self.title}, Artist: {self.artist}, Duration: {self.duration}")


class MusicLibrary:
    def __init__(self):
        self.songs = []

    def add_song(self, title, artist, duration):
        song = Song(title, artist, duration)
        self.songs.append(song)

    def display_songs(self):
        print(f"Songs in the library:")
        for song in self.songs:
            song.display_song()
    # Working better
    def find_songs_by_artist(self, artist):
        artist_songs = [song for song in self.songs if song.artist == artist]
        if artist_songs:
            print("Artist songs:")
            for song in artist_songs:
                print(f"Title: {song.title}, Artist: {song.artist}, Duration: {song.duration} minutes")
        else:
            print(f"No songs found for artist {artist}")

    # Own attempt
    #def find_artist_song(self, artist_name):
        #for song in self.songs:
            #if song.artist == artist_name:
                #print("We found the song!")
                #song.display_song()
                #break
            #else:
                #print("Unfortunately, no songs like this")



music_library = MusicLibrary()
music_library.add_song("Hey", "Kylie Minogue", "3:12")
music_library.add_song("Bye", "Britney Spears", "2:15")
music_library.add_song("Hi again", "JLO", "1:59")

music_library.display_songs()
music_library.find_songs_by_artist("Britney Spears")

# ChatG company class
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary


class Company:
    def __init__(self):
        self.employees = []

    def add_employees(self, name, position, salary):
        self.employees.append(Employee(name, position, salary))

    def calculate_total_salaries(self):
        salary = 0
        for employee in self.employees:
            salary += employee.salary
        print(f"Total salary of employees: {salary}")

    def find_highest_salary(self):
        highest_salary = self.employees[0]
        for employee in self.employees:
            if employee.salary > highest_salary.salary:
                highest_salary = employee
        print(f"Highest salary: {highest_salary.salary}")


new_company = Company()
new_company.add_employees("John Johnson", "Assistant", 2500)
new_company.add_employees("Anna", "Assistant", 2400)
new_company.add_employees("Tim Timm", "Manager", 4000)
new_company.calculate_total_salaries()
new_company.find_highest_salary()

# ChatG school
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject


class School:
    def __init__(self):
        self.students = []
        self.teachers = []

    def enroll_student(self, name, age):
        student = Student(name, age)
        self.students.append(student)

    def hire_teacher(self, name, subject):
        teacher = Teacher(name, subject)
        self.teachers.append(teacher)

    def display_students(self):
        print("Students present:")
        for student in self.students:
            print(f"Name: {student.name} Age: {student.age}")

    def display_teachers(self):
        print("Teaching at school:")
        for teacher in self.teachers:
            print(f"Name: {teacher.name} Subject: {teacher.subject}")


new_school = School()
new_school.enroll_student("Julija I.", 26)
new_school.enroll_student("Tim Timmo", 20)
new_school.enroll_student("Anna C.", 19)
new_school.hire_teacher("Gibi Giniot", "Mathematics")
new_school.hire_teacher("Sun Saulin", "English language")
new_school.display_students()
new_school.display_teachers()

