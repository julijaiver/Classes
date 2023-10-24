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
        self.elevators = [Elevator(top_floor, bottom_floor) for i in range(num_of_elevators)]
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
