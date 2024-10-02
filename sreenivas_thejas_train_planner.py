class Locomotive:
    def __init__(self, length, max_payload, max_speed):
        self.length = length
        self.max_payload = max_payload
        self.max_speed = max_speed

    def get_length(self):
        return self.length

    def get_maximum_payload(self):
        return self.max_payload

    def get_maximum_speed(self):
        return self.max_speed


class Railcar:
    def __init__(self, length, cargo_type, min_weight, max_weight, capacity):
        self.length = length
        self.cargo_type = cargo_type
        self.min_weight = min_weight
        self.max_weight = max_weight
        self.capacity = capacity
        self.current_weight = min_weight

    def get_length(self):
        return self.length
    
    def get_weight(self):
        return self.current_weight

    def get_cargo_type(self):
        return self.cargo_type


class Train:
    def __init__(self):
        self.locomotives = []
        self.cars = []

    def remove_locomotive(self):
        if len(self.locomotives) > 1:
            self.locomotives.pop()

    def add_locomotive(self, locomotive):
        self.locomotives.append(locomotive)

    def add_railcar(self, railcar):
        current_payload = sum([car.current_weight for car in self.cars])
        if current_payload + railcar.current_weight <= self.get_maximum_payload():
            self.cars.append(railcar)

    def get_payload(self):
        return sum([car.current_weight for car in self.cars])

    def get_length(self):
        return sum([loco.get_length() for loco in self.locomotives] + [car.get_length() for car in self.cars])

    def remove_railcar(self):
        if self.cars:
            self.cars.pop()

    def get_maximum_payload(self):
        return sum([loco.get_maximum_payload() for loco in self.locomotives])

    def get_speed(self):
        max_speeds = [loco.get_maximum_speed() for loco in self.locomotives]
        return min(max_speeds) * (1 - self.get_payload() / self.get_maximum_payload())

    def print_train(self):
        print("Payload:", self.get_payload(), "tons")
        print("Speed:", self.get_speed(), "mph")
        print("Length:", self.get_length(), "meters")
        print("..".join([loco.__class__.__name__[0] for loco in self.locomotives]), end="..")
        for car in self.cars:
            print(car.get_cargo_type()[0], end="..")
        print()

#Inputs:
loco1 = Locomotive(22, 120, 110)

car1 = Railcar(50, "Passenger", 20, 40, 1)
car2 = Railcar(100, 'Passenger', 30, 50, 1)
car3 = Railcar(90, "Freight", 15, 60, 1)
car4 = Railcar(80, 'Frieght', 20, 60, 1)

train = Train()
train.add_locomotive(loco1)
train.add_railcar(car1)
train.add_railcar(car2)
train.add_railcar(car3)
train.add_railcar(car4)
train.print_train()
