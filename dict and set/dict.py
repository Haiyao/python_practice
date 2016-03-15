# -*- coding: utf-8 -*-
d = {'Michel':95,'Bob':75,'Tracy':65,'Bob':85}
print(d['Michel'])

d['Adam'] = 67
print(d['Adam'])
print('tom' in d)
print('Adam' in d)

print(d.get('tom'))
print(d.get('tom',-2))

print(d)
d.pop('Bob')
print(d)
