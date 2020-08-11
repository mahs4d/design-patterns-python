"""
https://sourcemaking.com/design_patterns/command
"""

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass


class FunctionCommand(Command):
    def __init__(self, func):
        self._func = func

    def execute(self, *args, **kwargs):
        return self._func(*args, **kwargs)


# region usage

def hello_name(name):
    print(f'hello {name}')


if __name__ == '__main__':
    c1 = FunctionCommand(hello_name)
    c2 = FunctionCommand(hello_name)
    c3 = FunctionCommand(hello_name)
    c4 = FunctionCommand(hello_name)

    c1.execute('mahdi')
    c2.execute('mehrshad')
    c3.execute('mehran')
    c4.execute('ahmad')

# endregion
