class Student:
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        return f"My name is {self.name}"


print(Student("Nick"))
