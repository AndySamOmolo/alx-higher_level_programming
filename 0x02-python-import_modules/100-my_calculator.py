#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    i = len(sys.argv) - 1
    if i != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if op == "+":
        res = add(a, b)
    elif op == "-":
        res = sub(a, b)
    elif op == "*":
        res = mul(a, b)
    elif op == "/":
        res = div(a, b)

    print("{} {} {} = {}".format(a, op, b, res))
