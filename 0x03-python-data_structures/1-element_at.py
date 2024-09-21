#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        i = my_list.index(idx)
        print("Element at index {:d} is {}".format(idx, my_list[i]))
