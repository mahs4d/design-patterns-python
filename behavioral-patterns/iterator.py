class TrainIterator:
    def __init__(self, train):
        self.number_of_wagons = train.number_of_wagons
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.number_of_wagons:
            self.i += 1
            return self.i - 1

        raise StopIteration


class Train:
    def __init__(self, number_of_wagons):
        self.number_of_wagons = number_of_wagons

    def __iter__(self):
        return TrainIterator(self)


# region usage

if __name__ == '__main__':
    train = Train(10)
    for wagon in train:
        print(wagon)

    print('iterate for second time')

    for wagon in train:
        print(wagon)

# endregion
