
from . import cat
from . import dog

def animal(type):
  if type == 'cat':
    return cat.Cat()

  if type == 'dog':
    return dog.Dog()


