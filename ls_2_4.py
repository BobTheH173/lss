import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Study")
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print("Sleep")
        self.gladness += 3

    def to_rest(self):
        print("Rest")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out..")
            self.alive = False
        elif self.progress < -0:
            print("Depression..")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally..")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + "'s life"
        print(f"{day:-^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_rest()
            self.end_of_day()
            self.is_alive()


def start_life(name):
    name = Student(name=name)
    for day in range(365):
        if not name.is_alive:
            break
        name.live(day)


start_life(input("Input a name - "))
