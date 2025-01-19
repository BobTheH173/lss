class Student:
    def __init__(self, name=None, height=160):
        self.name = name
        self.height = height

    def __bool__(self):
        return self.name is not None

    def __len__(self):
        return self.height


nick = Student("Nick", height=170)

print(nick.__bool__())
print(nick.__bool__())
print(len(nick))
print(bool(nick))
