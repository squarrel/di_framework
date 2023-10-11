from abstract import Vacuum
import atexit
from settings import dependencies
from shop import Cart


class Container:
    def __init__(self):
        self.dependencies = []
        for name, dependency in dependencies:
            dep_instance = dependency(self)
            if not isinstance(dep_instance, Vacuum):
                raise ValueError("Container dependencies should be instances of Vacuum class.")

            setattr(self, name, dep_instance)
            self.dependencies.append(dep_instance)

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
