result = []


def divider(a, b):
    if a < b:
        raise ValueError
    if b > a:
        raise IndexError
    if a == 0 or b == 0:
        raise ZeroDivisionError

    return a / b


data = {10: 2, 5: 2, 123: 4, 18: 3, 15: 15, 8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
