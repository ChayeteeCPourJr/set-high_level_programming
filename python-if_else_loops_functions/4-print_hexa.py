#!/usr/bin/python3
for i in range(99):
    print("{:d} = {:#x}".format(i, i), end="" if i == 98 else ", ")
