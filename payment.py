from database import Db
from shop import Item, Cart


class Card:
    def __init__(self, number: int, first_name: str, last_name: str, address: str):
        self.number = number
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Payment:
    def __init__(self, container, cart: Cart, card: Card):
        self.container = container
        self.cart = cart
        self.card = card

    def charge(self):
        try:
            self.container.db.insert(
                'payments',
                self.cart.get_items(),
                self.cart.calc_cost(),
                self.card.number
            )
            print('Charged!')
            return True
        except Exception as e:
            print(str(e))
            return False


