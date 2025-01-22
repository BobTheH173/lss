class Human:
    def __init__(self, name="Human"):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers_names(self):
        if self.passengers:
            print(f"Names of {self.brand} passengers: ")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")


nick = Human("Nick")
kate = Human("Kate")
mike = Human("Mike")
john = Human("John")

car = Auto("Bentley")

car.add_passenger(nick, kate, mike, john)
car.print_passengers_names()
