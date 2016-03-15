# -*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
    w = b**2-4*a*c
    if w >= 0:
        x1 = (-b+math.sqrt(w))/2*a
        x2 = (-b-math.sqrt(w))/2*a
        return x1
        return x2
    else:
        return 'false'
