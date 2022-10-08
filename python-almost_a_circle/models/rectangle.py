#!/usr/bin/python3
''' First rectangle
'''

from models.base import Base


class Rectangle(Base):
    '''class Rectangle inherits from base
    '''
    KV_dict = {'id': 'id', 'width': '_Rectangle__width',
               'height': '_Rectangle__height',
               'x': '_Rectangle__x', 'y': '_Rectangle__y'}

    def __init__(self, width, height, x=0, y=0, id=None):
        '''method __init__ Initialization a Rectangle
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
