from database import Db
from payment import Payment
import notification import Mail


if __name__ == '__main__':
    db = Db('127.0.0.1', 993, 'user', 'passwd')
    mail = Mail('127.0.0.1', 993, 'user', 'passwd')

    item_1 = Item(item_id=124, color='red', amount=2, price=2.44)
    item_2 = Item(item_id=56, color='blue', amount=4, price=1.22)
    item_3 = Item(item_id=88, color='white', amount=5, price = 4.00)
    cart = Cart([item_1, item_2, item_3])

    card = Card(number, first_name, last_name, address)
    payment = Payment(cart: Cart, card: Card, db: Db)
    payment.charge()

    msg = 'Successful purchase!'
    mail.send(user.email_address, msg)
