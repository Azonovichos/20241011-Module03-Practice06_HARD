# Module 3 Practice HARD

def calculate_structure_sum (object):
  sum_object = 0

  if isinstance(object, (list, tuple, set)):
    for i in object:
      sum_object += calculate_structure_sum(i)
  elif isinstance(object, dict):
    for kwargs in object.items():
      sum_object += calculate_structure_sum(kwargs)
  elif isinstance(object, str):
    sum_object += len(object)
  elif isinstance(object, int):
    sum_object += object

  return sum_object

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

# Для опытов
print('\nFor examples')
'''print(type(data_structure))
print(len(data_structure))
print(isinstance(data_structure, list | tuple | dict))
if isinstance(data_structure, list | tuple | dict):
  data_structure_1 = [*data_structure]
  print(*data_structure_1)
'''