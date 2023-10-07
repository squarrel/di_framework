class Mail:
    server = None

    def __init__(self, address, port, username, password):
        self.address = address
        self.port = port
        self.username = username
        self.password = password
    
    def connect(self):
        return True

    def send(self, receiver: str, msg: str):
        return True

    def send(db: Db, receiver: str, msg: str):
        self.send(receiver, msg)
        db.insert('notifications', receiver, msg)
