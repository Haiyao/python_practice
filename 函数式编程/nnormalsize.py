# -*- coding: utf-8 -*-
#名字格式规范化。首字母大写。
L1 = ['adam', 'LISA', 'barT']
def normalsize(name):
    list(name)
    return name[0].upper() + name[1:].lower()
f = map(normalsize,L1)
print(list(f))