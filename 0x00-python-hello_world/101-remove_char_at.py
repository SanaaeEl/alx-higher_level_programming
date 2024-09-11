#!/usr/bin/python3
def remove_char_at(str, n):
    for i, ch in enumerate(str):
        if (i == n):
            continue
        else:
            copy = copy + ch
    return copy
