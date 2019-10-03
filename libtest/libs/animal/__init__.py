
from . import cat
from . import dog

def animal(type, name):
  if type == 'cat':
    return cat.Cat(name)

  if type == 'dog':
    return dog.Dog(name)

