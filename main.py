from payment import Card, Payment
from shop import Cart, Item, User


if __name__ == '__main__':
    user = User('Milos', 'Bulatovic', 'Street 38', '00381234567', 'milos@mail.com')

    item_1 = Item(item_id=124, color='red', amount=2, price=2.44)
    item_2 = Item(item_id=56, color='blue', amount=4, price=1.22)
    item_3 = Item(item_id=88, color='white', amount=5, price = 4.00)

    cart = Cart([item_1, item_2, item_3])
    card = Card(1234566543211234, 'Milos', 'Bulatovic', 'Address 58')
    payment = Payment(cart, card)

    charged = payment.charge()
    if charged:
        msg = 'Successful purchase!'
        payment.c.mail.send(user.email, msg)
