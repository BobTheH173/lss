import colorama
import inspect

for name, obj in inspect.getmembers(colorama):
    print(f"{name}: {obj}")
