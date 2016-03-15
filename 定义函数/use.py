# -*- coding: utf-8 -*-
from abs import my_abs
from abs import move
import math

c = input()
print(my_abs(c))

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)