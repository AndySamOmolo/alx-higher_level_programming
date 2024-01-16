#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_int = str(number)[-1]

if int(last_int) > 5:
    print(f"Last digit of {number} is {last_int} and is greater than 5")
elif int(last_int) == 0:
    print(f"Last digit of {number} is {last_int} and is 0")
elif int(last_int) != 0 and int(last_int) < 6:
    print(f"Last digit of {number} is {last_int} and is less than 6 and not 0")
