#!/usr/bin/python
def islower(c):
    c = input("Enter the letter")

    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False