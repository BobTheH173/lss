def checker(var_1):
    if type(var_1) is not str:
        raise TypeError(f"We can't work with {type(var_1)}")
    else:
        return var_1


# first_var = 32
# first_var = 10.22
first_var = "Hello"

checker(first_var)
print(first_var)
