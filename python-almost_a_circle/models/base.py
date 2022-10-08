#!/usr/bin/python3
''' models/base.py
'''


import json


class Base:
    ''' first class Base
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' initialize Base  __init__
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
