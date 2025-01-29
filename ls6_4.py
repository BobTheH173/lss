try:
    try:
        print("start code")
        print(error)
        print("No errors")
    except SyntaxError:
        print("SyntaxError")
except NameError as error:
    print(error)

print("code after capsule")
