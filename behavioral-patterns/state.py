"""
https://sourcemaking.com/design_patterns/state
"""

from abc import ABC, abstractmethod


class StateMachine:
    def __init__(self, initial_state):
        self._state = initial_state
        print(self._state)

    def set_state(self, state):
        self._state = state

    def step(self):
        self._state.step(self)
        print(self._state)


class State(ABC):
    @abstractmethod
    def step(self, machine):
        pass


# region usage

class State1(State):
    def step(self, machine):
        machine.set_state(State2())

    def __str__(self):
        return 'state1'


class State2(State):
    def step(self, machine):
        machine.set_state(State1())

    def __str__(self):
        return 'state2'


if __name__ == '__main__':
    initial_state = State1()
    machine = StateMachine(initial_state)
    machine.step()
    machine.step()
    machine.step()
    machine.step()
    machine.step()

# endregion
