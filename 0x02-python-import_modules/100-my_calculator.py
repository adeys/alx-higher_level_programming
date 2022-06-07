#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div


def main():
    argc = len(argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = argv[2]

    if operator not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if operator == "+":
        func = add
    elif operator == "-":
        func = sub
    elif operator == "*":
        func = mul
    elif operator == "/":  # This is obvious
        func = div

    a = int(argv[1])
    b = int(argv[3])

    print("{:d} {} {:d} = {:d}".format(a, operator, b, func(a, b)))


if __name__ == "__main__":
    main()
