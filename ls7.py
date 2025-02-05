my_list = [1, 2, 3]
iterator = iter(my_list)

print(iterator, "\n")

# print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print("\n")
for elem in iterator:
    print(elem)
