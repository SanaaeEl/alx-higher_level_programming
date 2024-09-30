#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return list(map(lambda elmnt: elmnt if elmnt != search else replace, my_list))
