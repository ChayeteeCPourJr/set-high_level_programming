#!/usr/bin/python3
"""Uses calculator_1's functions to handle a basic calculation
given as command-line arguments: <a> <operator> <b>"""
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    operators = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
    }

    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, op, b, operators[op](a, b)))
