# -*- coding: utf-8 -*-
import math

def my_abs(x):
    #参数类型检查
    if not isinstance(x,(int,float)):
        raise TypeError('cao')
    #函数内容
    if x>=0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny