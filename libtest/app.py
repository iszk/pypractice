#!/bin/env python

from libs import animals
from libs import repository
# from libs import company

animals.animal('cat', 'tama').say()
animals.animal('dog', 'pochi').say()

employees = repository.company_employees()

print(employees)
