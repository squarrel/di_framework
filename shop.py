class Cart:
    def __init__(self, items: List[Item]):
        self.items = items

    def get_items(self):
        return items

    def calc_cost(self):
        cost = 0
        for item in self.items:
            cost += item.price * item.amount


class Item:
    def __init__(self, item_id, color, amount, price):
        self.item_id = item_id
        self.color = color
        self.amount = amount
        self.price = price
