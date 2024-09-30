#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for st in sorted(a_dictionary):
        print("{}: {}". format(st, a_dictionary[st]))
