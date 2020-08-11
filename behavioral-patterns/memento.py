"""
https://sourcemaking.com/design_patterns/memento
"""

import pickle


class SavableClass:
    def __init__(self, somevar):
        self.somevar = somevar

    def print_somevar(self):
        print(f'somevar: {self.somevar}')

    def get_memento(self):
        return pickle.dumps(self)

    @staticmethod
    def from_memento(memento):
        return pickle.loads(memento)


# region usage

if __name__ == '__main__':
    a = SavableClass('hello')
    memento = a.get_memento()
    del a

    b = SavableClass.from_memento(memento)
    b.print_somevar()

# endregion
