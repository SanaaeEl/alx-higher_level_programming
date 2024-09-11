#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    for i, ch in enumerate(str):
        if i != n:
            copy += ch
    return copy
