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
      f"Registration number: {new_car.reg_number}\nMaximum speed: {new_car.max_speed} km/h"
      f"Current speed: {new_car.current_speed}")


