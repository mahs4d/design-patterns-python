from abc import ABC, abstractmethod


class Abstraction:
    def __init__(self, impl):
        self._impl = impl

    def hello(self):
        self._impl.hello()


class Implementation(ABC):
    @abstractmethod
    def hello(self):
        pass


class ImplementationA(Implementation):
    def hello(self):
        print('hello A')


class ImplementationB(Implementation):
    def hello(self):
        print('hello B')


# region usage

if __name__ == '__main__':
    Abstraction(ImplementationA()).hello()

# endregion
