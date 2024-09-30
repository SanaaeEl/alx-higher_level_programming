#!/usr/bin/python3

def best_score(a_dictionary):
    best = a_dictionary[0]
    for key, score in a_dictionary:
        if score > best.keys:
            best = a_dictionary[key]
    return best

