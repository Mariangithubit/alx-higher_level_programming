#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    temp = a_dictionary.copy()
    for c, i in temp.items():
        if value == i:
            a_dictionary.pop(c)
    return a_dictionary
