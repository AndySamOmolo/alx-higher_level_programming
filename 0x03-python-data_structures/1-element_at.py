#!/usr/bin/python3
def element_at(my_list, idx):
  if idx < 0:
    return None
  elif idx > len(my_list):
    return None
  print("Elelment at index {:d} is {}".format(idx, my_list[idx]))
