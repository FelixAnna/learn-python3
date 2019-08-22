#! /usr/bin/env python3

"""
This part show you
How to use the module we just defined
"""

from a_16_module import *

print(fib(10) == 55)


from a_16_module import fib
print(fib(9) == 34)

import sys

print(sys.path)

for i in sys.argv:
    print(i)

b=dir()
print(b)
print('__name__' in b)
print('fib' in b)
print('pi' in b)

c=dir(sys)
print('path' in c)

