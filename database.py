class Db:
    def __init__(self, address, port, username, password):
        self.address = address
        self.port = port
        self.username = username
        self.password = password

    def connect(self):
        return True

    def get(self, table_name: str):
        return {}

    def insert(self, table_name: str, *args):
        return True
