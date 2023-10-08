from typing import List


class Item:
    def __init__(self, item_id: int, color: str, amount: int, price: int):
        self.item_id = item_id
        self.color = color
        self.amount = amount
        self.price = price

    def get_price(self):
        return 15.00


class Cart:
    def __init__(self, items: List[Item]):
        self.items = items

    def get_items(self):
        return [item.item_id for item in self.items]

    def calc_cost(self):
        cost = 0
        for item in self.items:
            cost += item.price * item.amount
        return round(cost)


class User:
    def __init__(self, first_name: str, last_name: str, address: str, phone: int, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.address =  address
        self.phone = phone
        self.email = email
