from abstract import Vacuum
import atexit
from settings import dependencies
from shop import Cart


class Container:
    def __init__(self):
        self.dependencies = []
        for d in dependencies:
            self.__dict__[d[0]] = d[1](self)
            self.dependencies.append(self.__dict__[d[0]])

            if not isinstance(self.__dict__[d[0]], Vacuum):
                raise ValueError("Container dependencies should be instances of Vacuum class.")

    def open(self):
        for d in self.dependencies:
            d.start()

    def close(self):
        for d in self.dependencies:
            d.stop()

    def __del__(self):
        self.close()


def di(func):
    def func_wrapper(*args, **kwargs):
        container = Container()
        container.open()
        func.c = container
        return func(*args, **kwargs)
    return func_wrapper
