#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    ln = len(sys.argv) - 1
    if ln == 0:
        print("0 arguments")
    elif ln == 1:
            print("{} argument:".format(ln))
    else:
            print("{} arguments:".format(ln))
    for i in range(1, ln+1):
            print("{}: {}".format(i, sys.argv[i]))
