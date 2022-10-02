#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy = a_dictionary.copy()
    for key in copy:
        if copy[key] == value:
            del a_dictionary[key]
    return a_dictionary
