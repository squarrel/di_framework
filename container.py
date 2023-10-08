from database import Db
from notification import Mail
from payment import Card
from shop import Cart


dependencies = (('db', Db), ('mail', Mail))


class Container:
    def __init__(self):
        self.dependencies = []
        for d in dependencies:
            self.__dict__[d[0]] = d[1](self)
            self.dependencies.append(self.__dict__[d[0]])

    def open(self):
        for d in self.dependencies:
            d.start()

    def close(self):
        for d in self.dependencies:
            d.stop()
