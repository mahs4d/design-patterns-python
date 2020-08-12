"""
https://sourcemaking.com/design_patterns/composite
"""

from abc import ABC, abstractmethod


class Component:
    def __init__(self):
        self._children = []

    def add_child(self, child):
        self._children.append(child)

    def draw(self):
        for child in self._children:
            child.draw()


class SubComponent(ABC):
    @abstractmethod
    def draw(self):
        pass


# region usage

class C1(SubComponent):
    def draw(self):
        print('draw c1')


if __name__ == '__main__':
    component = Component()
    component.add_child(C1())
    component.add_child(C1())
    component.add_child(C1())
    component.add_child(C1())
    component.add_child(C1())
    component.draw()

# endregion
