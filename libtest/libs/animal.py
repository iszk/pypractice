
import sys

from . import animals

def animal(type, name):
  if type == 'cat':
    return animals.cat.Cat(name)

  if type == 'dog':
    return animals.dog.Dog(name)

