#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:
            u = chr(ord(u) - 32)
        print("{:s}".format(u), end="")
    print()
