# -*- coding: utf-8 -*-
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A','',None,' '])))

#求素数-埃式筛法
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def prime():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it =filter(_not_divisible(n),it)

for n in prime():
    if n < 1000:
        print(n)
    else:
        break