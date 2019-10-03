
from . import utils

class Dog(utils.Animal):

  def say(self):
    print('bow, i am ' + self.get_name())
