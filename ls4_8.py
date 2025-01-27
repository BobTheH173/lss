class Scan:
    def __init__(self):
        print("Scanning..")


class Print(Scan):
    def __init__(self):
        super().__init__()
        print("Printing..")


class Printer(Print):
    pass


printer = Printer()
