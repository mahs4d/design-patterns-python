class Adaptee:
    def hello(self):
        print('hi')


class Adapter:
    def __init__(self):
        self._adaptee = Adaptee()

    def hello(self):
        self._adaptee.hello()


# region usage

if __name__ == '__main__':
    Adapter().hello()

# endregion
