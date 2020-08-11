"""
https://sourcemaking.com/design_patterns/object_pool
http://effbot.org/zone/thread-synchronization.htm
"""

from threading import Lock, BoundedSemaphore


class Reusable:
    def __init__(self, id):
        self._id = id

    def __str__(self):
        return f"reusable id: {self._id}"


class ReusablePool:
    def __init__(self, max_size=10):
        self._max_size = max_size
        self._instances = []
        self._created_instances = 0

        self._creation_lock = Lock()
        self._semaphore = BoundedSemaphore(max_size)

    def acquire(self):
        self._semaphore.acquire()
        if self._created_instances < self._max_size:
            with self._creation_lock:
                if self._created_instances < self._max_size:
                    self._created_instances += 1
                    return Reusable(id=self._created_instances)

        return self._instances.pop()

    def release(self, reusable):
        self._instances.append(reusable)
        self._semaphore.release()


# region usage

if __name__ == "__main__":
    pool = ReusablePool(2)

    a = pool.acquire()
    b = pool.acquire()
    print(a)
    print(b)
    pool.release(b)
    c = pool.acquire()
    print(c)

    d = pool.acquire()
    print(d)

# endregion
