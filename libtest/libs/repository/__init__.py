from . import company
from .. import animals

def company_employees():
  c = company.Company()
  es = c.employee_list()

  ret = []
  for e in es:
    a = animals.animal(e['type'], e['name'])
    ret.append(a)

  return ret

