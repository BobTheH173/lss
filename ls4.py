class Human:
    height = 170
    satiety = 50


class Student(Human):
    satiety = 0


class Worker(Human):
    satiety = 100


nick = Student()
ann = Worker()

print(nick.satiety)
print(ann.satiety)
