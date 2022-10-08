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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file"""
        if list_objs is None:
            json_string = "[]"
        else:
            json_string = cls.to_json_string([obj.to_dictionary()
                                              for obj in list_objs])
        with open(cls.__name__ + '.json', mode='w+',
                  encoding='utf-8') as a_file:
            a_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)
