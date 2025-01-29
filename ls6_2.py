try:
    print("start code")
    print(10 / 0)
    print("No errors")
except NameError:
    print("We have an error - NameError")
except ZeroDivisionError:
    print("We have an error - ZeroDivisionError")

print("code after capsule")
