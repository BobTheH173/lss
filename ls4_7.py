class Computer:
    def __init__(self):
        super().__init__()
        memory = 128


class Display:
    def __init__(self):
        super().__init__()
        resolution = "4k"


class Phone(Display, Computer):
    def print_info(self):
        print(self.resolution)
        print(self.memory)


iphone = Phone()

iphone.print_info()
