# -*- coding: utf-8 -*-

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

x = input('enter you number')
x = int(x)

f = fib(x)
print(f)

for n in fib(x):
    print(n)