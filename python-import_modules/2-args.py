#!/usr/bin/python3
from sys import argv


def main():
    argc = len(argv) - 1

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
