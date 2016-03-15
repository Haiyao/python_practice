# -*- coding: utf-8 -*-
from functools import reduce

def prod(number):
    def built(x,y):
        return x * y
    return reduce(built,number)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))