from abstract import Vacuum


class Db(Vacuum):
    def __init__(self, container):
        self.container = container

    def start(self):
        '''Connects the database.'''
        address = '127.0.0.1'
        port = 5432
        username = 'user'
        password = 'passwd'
        print('Connected database.')
        return True

    def stop(self):
        '''Disconnects database.'''
        print('Disconnected database.')
        return True

    def get(self, table_name: str):
        return {}

    def insert(self, table_name: str, *args):
        print('Inserting arguments {} into table {}.'.format(args, table_name))
        return True
