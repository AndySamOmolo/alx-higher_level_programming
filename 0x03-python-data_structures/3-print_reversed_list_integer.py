#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
  i = len(my_list) - 1
  for n in my_list[i]:
    if i < 0:
      return
    print("{}".format(n))
    i--
