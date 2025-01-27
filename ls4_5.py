class Grandparent:
    @staticmethod
    def about():
        print("I'm Grandparent")

    def about_myself(self):
        print("I'm Grandparent")


class Parent(Grandparent):
    def about_myself(self):
        print("I'm Parent")


class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()


nick = Child()
