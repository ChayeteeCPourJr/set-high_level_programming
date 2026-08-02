#!/usr/bin/python3
for i in range(97, 123):
    print("{}".format(chr(i)), end="") if chr(i) != "q" and chr(i) != "e" else None
