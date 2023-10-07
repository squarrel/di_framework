from database import Db
from shop import Item, Cart


class Card:
    def __init__(self, number: int, first_name: str, last_name: str, address: str):
        self.number = number
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Payment:
    def __init__(self, cart: Cart, card: Card, db: Db):
        self.cart = cart
        self.card = card
        self.db = db

    def charge(self):
        try:
            self.db.insert(
                'payments',
                self.cart.get_items(),
                self.cart.calc_cost(),
                self.card.get_id()
            )
            return True
        except:
            return False


