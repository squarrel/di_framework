# Dependency Injection Framework

## Usage

Register dependencies inside container.py file. For user-defined classes to have access to the container, use the @di decorator.

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
#container.py
from somewhere import Service

dependencies = (('db', Db), ('mail', Mail), ('service', 'Service'))
```
```
user = User()
user.c.service('some_param')
```
