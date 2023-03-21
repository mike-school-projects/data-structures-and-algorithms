import math

def insert_shift_list(lst, value):
  if type(lst) is not list:
    return 'not a list'
  middle = math.ceil(len(lst) / 2)

  new_list = lst[:(middle)]
  new_list.append(value)
  new_list.extend(lst[middle:])
  return new_list


items = [1, 2 ,3, 4]
print(insert_shift_list(items, 'test'))
