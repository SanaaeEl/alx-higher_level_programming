#!/usr/bin/python3
import sys
l = len(sys.argv) - 1
if l == 0:
    print("0 arguments")
elif l > 1:
    if l == 1:
        print("{} argument:".format(l))
    else:
        print("{} arguments:".format(l))
    for i, arg in enumerate(sys.argv):
        if (i > 0):
            print("{}: {}".format(i, arg))