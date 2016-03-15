# -*- coding: utf-8 -*-
f = abs
print(f(-15))

def add(x, y, f):
    return f(x) + f(y)

print(add(5, -6, f))