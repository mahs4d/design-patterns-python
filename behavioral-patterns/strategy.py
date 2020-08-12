from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def algorithm(self):
        pass


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def get_result(self):
        return self._strategy.algorithm()


# region usage

class MyStrategy(Strategy):
    def algorithm(self):
        return 12


if __name__ == '__main__':
    strategy = MyStrategy()
    context = Context(strategy)
    print(context.get_result())

# endregion
