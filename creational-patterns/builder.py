"""
https://sourcemaking.com/design_patterns/builder
"""


class Car:
    def __init__(self, name, color):
        self._name = name
        self._color = color

    def __str__(self):
        return f"{self._name}:{self._color}"


class CarBuilder:
    def __init__(self):
        self._name = ""
        self._color = ""

    def set_color(self, color):
        self._color = color
        return self

    def set_name(self, name):
        self._name = name
        return self

    def build(self):
        return Car(self._name, self._color)


# region main

if __name__ == "__main__":
    my_car = CarBuilder().set_name("pride").set_color("red").build()
    print(my_car)

# endregion
