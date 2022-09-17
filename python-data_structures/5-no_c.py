#!/usr/bin/python3
def no_c(my_string):
    my_new_str = ""
    for i in my_string:
        if i != 'C' and i != 'c':
            my_new_str += i
    return my_new_str
