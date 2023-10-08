# Dependency Injection Framework

## Usage

Register dependencies inside container.py file. For user-defined classes to have access to the container, use the @di decorator.

### Example Usage
```
from container import di  
  
@di
class User:
    pass

user = User()
user.c.mail.send('support@mail.com', 'Message')
```
