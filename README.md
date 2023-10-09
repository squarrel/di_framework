# Dependency Injection Framework

## Usage

Register dependencies in settings.py file. For user-defined classes to have access to the container, use the @di decorator.

### Example Using @di decorator
```
from container import di

@di
class User:
    pass

user = User()
user.c.mail.send('support@mail.com', 'Message')
```

### Example adding new dependency to container
```
#service.py
from abstract import Vacuum

class Service(Vacuum):
    def __init__(self, container):
        self.container = container

    def start(self):
        ```do something```

    def stop(self):
        ```do something```

    def do(self):
        ```do something```
```
```
#settings.py
from service import Service

dependencies = (('db', Db), ('mail', Mail), ('service', 'Service'))
```
```
user = User()
user.c.service.do('some_param')
```
