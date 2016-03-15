# -*- coding: utf-8 -*-
def add_end(L=[]):
    L.append('END')
    return L
print(add_end([1, 2, 3]))
print(add_end())
print(add_end())

#默认参数必须指向不变量
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end([1, 2, 3]))
print(add_end())
print(add_end())