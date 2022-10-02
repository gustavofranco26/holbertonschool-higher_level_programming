#!/usr/bin/python3

"""Defines an inherited list class MyList."""


class MyList(list):
    """
    MyList class inherited from builtin list class
    """
    def print_sorted(self):
        """
        Prints a sorted list
        """
        print(sorted(self))
