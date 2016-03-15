# -*- coding: utf-8 -*-
L = ['bob', 'about', 'Zoo', 'Credit']
l = sorted(L)
print(l)
print(sorted(L,key = str.lower,reverse=True))
print(sorted(L,key = str.lower))

#Practice
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#按名字排布
def name_by(s):
    a = s[0]
    return a

#按成绩排布
def source_by(s):
    b = s[1]
    return b 

print(sorted(L))
print(sorted(L,key = name_by))
print(sorted(L,key = source_by))