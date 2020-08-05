"""
https://sourcemaking.com/design_patterns/abstract_factory
https://medium.com/datadriveninvestor/usage-of-singleton-pattern-in-multithreaded-applications-ec0cc4c8805e
"""

from abc import ABC, abstractmethod


class Tv(ABC):
    pass


class Phone(ABC):
    pass


class AbstractFactory(ABC):
    @abstractmethod
    def create_tv(self) -> Tv:
        pass

    @abstractmethod
    def create_phone(self) -> Phone:
        pass


# region samsung


class RU7099Tv(Tv):
    def __str__(self):
        return "Samsung RU7099"


class GalaxyS10Phone(Phone):
    def __str__(self):
        return "Samsung Galaxy S10"


class SamsungFactory(AbstractFactory):
    def create_tv(self) -> Tv:
        return RU7099Tv()

    def create_phone(self) -> Phone:
        return GalaxyS10Phone()


# endregion

# region sony


class BraviaTv(Tv):
    def __str__(self):
        return "Sony Bravia"


class Xperia10Phone(Phone):
    def __str__(self):
        return "Sony Xperia 10"


class SonyFactory(AbstractFactory):
    def create_tv(self) -> Tv:
        return BraviaTv()

    def create_phone(self) -> Phone:
        return Xperia10Phone()


# endregion

# region main

if __name__ == "__main__":
    samsung_factory = SamsungFactory()
    sony_factory = SonyFactory()

    print(samsung_factory.create_phone())
    print(samsung_factory.create_tv())
    print(sony_factory.create_phone())
    print(sony_factory.create_tv())

# endregion
