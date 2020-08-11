"""
https://sourcemaking.com/design_patterns/singleton
"""

from threading import Lock


class MySingletonClass:
    _instantiation_lock = Lock()
    _instance = None

    @staticmethod
    def get_instance():
        # using double checked locking pattern, so that we use lock only if _instance is None
        if MySingletonClass._instance is None:
            with MySingletonClass._instantiation_lock:
                if MySingletonClass._instance is None:
                    # instantiation is performed here (after second null check)
                    MySingletonClass._instance = MySingletonClass()

        return MySingletonClass._instance

    def __init__(self):
        print("__init__ called")


# region usage

if __name__ == "__main__":
    a = MySingletonClass.get_instance()
    b = MySingletonClass.get_instance()

    assert a == b

# endregion
