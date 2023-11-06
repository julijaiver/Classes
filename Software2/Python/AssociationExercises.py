# Exercise 1
class Elevator:
    def __init__(self, top_floor, bottom_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1

    def floor_down(self):
        self.current_floor -= 1

    def go_to_floor(self, floor):
        while self.current_floor != floor:
            if floor < self.bottom_floor:
                print(f"Bottom floor is {self.bottom_floor}")
                break
            elif floor > self.top_floor:
                print(f"Top floor is {self.top_floor}")
                break
            if self.current_floor < floor:
                self.floor_up()
                print(f"Floor {self.current_floor}")
            elif self.current_floor > floor:
                self.floor_down()
                print(f"Floor {self.current_floor}")
        print(f"You are in {self.current_floor} floor")


elev1 = Elevator(12, 1)

# Exercise 2 and 3
class Elevator:
    def __init__(self, top_floor, bottom_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1

    def floor_down(self):
        self.current_floor -= 1

    def go_to_floor(self, floor):
        while self.current_floor != floor:
            if floor < self.bottom_floor or floor > self.top_floor:
                print("Invalid floor")
                break
            if self.current_floor < floor:
                self.floor_up()
                print(f"Floor {self.current_floor}")
            elif self.current_floor > floor:
                self.floor_down()
                print(f"Floor {self.current_floor}")
        print(f"You are in {self.current_floor} floor")


class Building:
    def __init__(self, bottom_floor, top_floor, num_of_elevators):
        self.elevators = [Elevator(top_floor, bottom_floor) in range(num_of_elevators)]
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def run_elevator(self, num_of_elevator, dest_floor):
        if num_of_elevator < 0 or num_of_elevator >= len(self.elevators):
            print("Invalid elevator number")
            return
        print(f"Running elevator {num_of_elevator} from floor {self.elevators[num_of_elevator - 1].current_floor}"
              f" to floor {dest_floor}")
        self.elevators[num_of_elevator - 1].go_to_floor(dest_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.current_floor = self.bottom_floor
        print(f"All elevators are on floor {self.bottom_floor}")

# Exercise 4

import random
from prettytable import PrettyTable


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


class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = []

        for i in range(cars):
            reg_num = f"ABC-{i + 1}"
            max_speed = random.randint(100, 200)
            car = Car(reg_num, max_speed)
            self.cars.append(car)


    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance_km:
                return True
        return False

    def print_status(self):
        table = PrettyTable()
        table.field_names = ["Registration Number", "Current speed", "Travelled distance"]
        for car in self.cars:
            table.add_row([car.reg_number, car.current_speed, car.travelled_distance])
        print(table)


new_race = Race("Grand Demolition Derby", 8000, 10)
stop = False
hours_passed = 0

while not new_race.race_finished():
    new_race.hour_passes()
    hours_passed += 1

    if hours_passed % 10 == 0:
        new_race.print_status()

new_race.print_status()
