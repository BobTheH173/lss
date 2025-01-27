class Hello:
    def __init__(self):
        print("Hello")


class World(Hello):
    def __init__(self):
        super().__init__()
        print("World!")


hello_world = World()
