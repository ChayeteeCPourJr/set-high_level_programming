#!/usr/bin/python3
def uppercase(str):
    for c in str:
        n = ord(c) - 32 if ord(c) >= 97 and ord(c) <= 122 else ord(c)
        print("{:c}".format(n), end="")
    print()
