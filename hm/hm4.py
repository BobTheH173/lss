import random


class Cipher:
    def __init__(self, number1):
        self._number1 = number1
        self._number2 = random.randint(1, number1)
        self._operation = random.choice(['+', '-', '*', '/'])
        self._result = eval(f"{self._number1} {self._operation} {self._number2}")

    def __str__(self):
        return str(self._result)


cipher = Cipher(int(input("Enter your number - ")))
print(cipher)
