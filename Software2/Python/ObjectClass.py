# Encapsulation, only the method in a class can change attributes

# One way (not the right way) Inconsistency of the attributes
class MyPet:
    pass


dog = MyPet()
dog.name = "Snowy"
dog.color = "white"
print(dog.name, dog.color)

cat = MyPet()
cat.name = "Chicco"
cat.color = "gray"
cat.age = 2
print(cat.color, cat.age)


# Other way
class MyPet:
    # if a variable shared between all objects, it should be class-based
    counter = 0
    def __init__(self, n, c):
        self.name = n
        self.color = c
        MyPet.counter += 1

# Setter and getter to manipulate through methods
    def setName(self, newName):
        self.name = newName
    # Getter usually for calculations
    def getName(self):
        return self.name

    def bark(self, n):
        for i in range(n):
            print("woof woof")


dog = MyPet("Snowy", "brown")
cat = MyPet("Chicco", "gray")
print(f"dog name: {dog.name}")
print(f"cat name: {cat.name}")

cat.setName("Unknown")
print(f"cat's new name: {cat.name}")

dog.bark(3)

print(f"number of pets: {MyPet.counter}")

# Exercise: white a student's class with the following attributes: student name, age, degree program.
# Add a constructor and proper functions to manipulate the attributes of students.
# Print the number of students attending your class
# Test your class by creating different objects

class Student:
    counter = 0

    def __init__(self, name, age, degree_program):
        self.name = name
        self.age = age
        self.program = degree_program
        Student.counter += 1

    def set_name(self, new_name):
        self.name = new_name


student1 = Student("Anna", 24, "IT")
student2 = Student("Tim", "25", "Comm")
student3 = Student("Bob", "19", "IT")

student2.set_name("Lana")
print(student2.name)
print(f"number of students: {Student.counter}")
