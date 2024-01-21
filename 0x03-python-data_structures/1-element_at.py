#!/usr/bin/python3
def element_at(my_list, idx):
  my_list = [1, 2, 3, 4, 5]
  idx = 3
  if idx < 0:
    return None
  elif idx > len(my_list):
    return None
  print("Elelment at index {:d} is {}".format(idx, my_list[idx]))
