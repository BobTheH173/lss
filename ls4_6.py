class Computer:
    @staticmethod
    def calculate():
        print("Calculating..")


class Display:
    @staticmethod
    def display():
        print("Displaying..")


class Phone(Computer, Display):
    pass


iphone = Phone()

iphone.calculate()
iphone.display()
