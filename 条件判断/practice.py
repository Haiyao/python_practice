# -*- coding: utf-8 -*-
height = 1.75
weight = 80.5
bml = 80.5/(1.75*1.75)
print(bml)
if bml < 18.5:
    print('过轻')
elif 18.5 <= bml < 25:
    print('正常')
elif 25 <= bml < 28:
    print('过重')
elif 28 <= bml < 32:
    print('肥胖')
else:
    print('严重肥胖')