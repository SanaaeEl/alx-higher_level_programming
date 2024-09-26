#!/usr/bin/python3

def multiple_returns(sentence):

    l = len(sentence)

    if sentence == '\0':
        first = "None"
    else:
        first = sentence[0]

    tup = (l, first)
    return tup
