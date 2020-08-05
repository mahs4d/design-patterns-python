import copy
from abc import ABC


class Clonable(ABC):
    def clone(self):
        return copy.deepcopy(self)


class Product(Clonable):
    def __init__(self, name):
        self._name = name

    def __str__(self) -> str:
        return self._name


# region main

if __name__ == "__main__":
    product1 = Product("p1")
    product2 = product1.clone()

    print(product2)
    product2._name = "p2"
    print(product1)
    print(product2)

# endregion
