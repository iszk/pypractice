
from . import utils

class Cat(utils.Animal):

  def say(self):
    print('mew, i am ' + self.get_name())

