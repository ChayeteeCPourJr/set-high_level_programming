#!/usr/bin/python3
import sys

argc = len(sys.argv) - 1

if argc == 0:
    print("0 arguments.")
elif argc == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(argc))

if argc >= 1:
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
