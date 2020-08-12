"""
https://sourcemaking.com/design_patterns/template_method
"""

from abc import ABC, abstractmethod


class Template(ABC):
    def run(self):
        self.step1()
        self.step2()
        self.step3()

    @abstractmethod
    def step1(self):
        pass

    def step2(self):
        print('step2')

    @abstractmethod
    def step3(self):
        pass


# region usage

class ConcreteTemplate(Template):
    def step1(self):
        print('c step1')

    def step3(self):
        print('c step3')


if __name__ == '__main__':
    ct = ConcreteTemplate()
    ct.run()

# endregion
