# Exercise 1
class Car:
    current_speed = 0
    travelled_distance = 0

    def __init__(self, reg_num, max_speed):
        self.reg_number = reg_num
        self.max_speed = max_speed

new_car = Car("ABC-123", "142 km/h")
print(f"Current speed: {Car.current_speed}\nTravelled distance: {Car.travelled_distance}\n"
      f"Registration number: {new_car.reg_number}\nMaximum speed: {new_car.max_speed}")

# Exercise 2
class Car:
    current_speed = 0
    travelled_distance = 0

    def __init__(self, reg_num, max_speed):
        self.reg_number = reg_num
        self.max_speed = max_speed

    def accelerate(self, speed_change):
        if 0 <= self.current_speed <= self.max_speed:
            self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0


new_car = Car("ABC-123", 142)
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
new_car.accelerate(-200)
print(f"Current speed: {Car.current_speed}\nTravelled distance: {Car.travelled_distance}\n"
      f"Registration number: {new_car.reg_number}\nMaximum speed: {new_car.max_speed} km/h\n"
      f"Current speed: {new_car.current_speed}")

# Exercise 3

class Car:
    current_speed = 0
    travelled_distance = 0

    def __init__(self, reg_num, max_speed):
        self.reg_number = reg_num
        self.max_speed = max_speed

    def accelerate(self, speed_change):
        if 0 <= self.current_speed <= self.max_speed:
            self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += (self.current_speed * hours)


new_car = Car("ABC-123", 142)
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
print(f"Current speed: {Car.current_speed}\nTravelled distance: {Car.travelled_distance}\n"
      f"Registration number: {new_car.reg_number}\nMaximum speed: {new_car.max_speed} km/h\n"
      f"Current speed: {new_car.current_speed}")

new_car.drive(3)
print(f"Travelled distance: {new_car.travelled_distance}")

new_car.drive(2)
print(f"Travelled distance: {new_car.travelled_distance}")

new_car.drive(1)
print(f"Travelled distance: {new_car.travelled_distance}")

# 4th exercise

import random


class Car:

    def __init__(self, reg_num, max_speed, current_speed=0, travelled_distance=0):
        self.reg_number = reg_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed_change):
        if 0 <= self.current_speed <= self.max_speed:
            self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += (self.current_speed * hours)


cars = []
for i in range(10):
    reg_num = f"ABC-{i+1}"
    max_speed = random.randint(100, 200)
    new_car = Car(reg_num, max_speed)
    cars.append(new_car)

stop = False
while not stop:
    for car in cars:
        car.drive(1)
        car.accelerate(random.randint(-10, 15))
        if car.travelled_distance > 10000:
            stop = True


for car in cars:
    print(f"Car {car.reg_number} Current speed: {car.current_speed} Travelled distance: {car.travelled_distance}")

