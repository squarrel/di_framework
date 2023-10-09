from abstract import Vacuum
from container import Container, di
from payment import Card, Payment
import pytest
from settings import dependencies
from shop import Cart, Item
from unittest import mock


@mock.patch('container.Container.open')
def test_start_method_called(mock_open):
    @di
    class Test:
        pass

    test = Test()

    assert mock_open.called


def test_payment_accesses_container():
    item_1 = Item(item_id=124, color='red', amount=2, price=2.44)
    item_2 = Item(item_id=56, color='blue', amount=4, price=1.22)
    item_3 = Item(item_id=88, color='white', amount=5, price = 4.00)

    cart = Cart([item_1, item_2, item_3])
    card = Card(1234566543211234, 'Milos', 'Bulatovic', 'Address 58')

    payment = Payment(cart, card)
    assert isinstance(payment.c, Container)


@pytest.fixture
def user():
    class User(Vacuum):
        def __init__(self, container):
            self.c = container

        def start(self):
            pass

        def stop(self):
            pass

    dependencies.append(('user', User))

    return User


def test_adding_new_dependency(user):
    item_1 = Item(item_id=124, color='red', amount=2, price=2.44)
    item_2 = Item(item_id=56, color='blue', amount=4, price=1.22)
    item_3 = Item(item_id=88, color='white', amount=5, price = 4.00)

    cart = Cart([item_1, item_2, item_3])
    card = Card(1234566543211234, 'Milos', 'Bulatovic', 'Address 58')

    payment = Payment(cart, card)
    assert isinstance(payment.c.user, user)
