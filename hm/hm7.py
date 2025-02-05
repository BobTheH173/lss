import string
import random


# def generator(letter_count):
#     return random.choices(string.ascii_lowercase, k=letter_count)
#
#
# print(generator(int(input("letter_count - "))))

def generator():
    while True:
        yield random.choice(string.ascii_lowercase)


generator = generator()
for _ in range(8):
    print(next(generator))
