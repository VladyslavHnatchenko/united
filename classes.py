class Person:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print("Hi, my name is", self.name)


class Auto:
    def __init__(self, name):
        self.name = name

    def move(self, speed):
        print(self.name, "move with speed", speed, "km/h")
