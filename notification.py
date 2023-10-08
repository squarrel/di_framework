from abstract import Vacuum
from database import Db


class Mail(Vacuum):
    def __init__(self, container):
        self.container = container

    def start(self):
        '''Connects the server.'''
        address = '127.0.0.1'
        port = 993
        username = 'user'
        password = 'passwd'
        print('Connected mail server.')
        return True

    def stop(self):
        '''Disconnects the server.'''
        print('Disconnected mail server.')
        return True

    def send(self, receiver: str, msg: str):
        print('Message {} sent to {}.'.format(msg, receiver))
        self.container.db.insert('notifications', receiver, msg)
