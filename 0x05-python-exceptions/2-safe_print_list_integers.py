#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for a in range(x):
        try:
            print("{:d}".format(my_list[a]), end="")
            couny += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            print("IndexError: list index out of range")
    print()
    return (count)
