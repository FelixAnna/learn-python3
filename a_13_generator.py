#! /usr/bin/env python3

"""
This part shows you
how to create a generator
in python3
"""

import sys

def fibonacci(n):
    a, b, c=0, 1, 0

    while c<n:
        yield a
        a, b=b, a+b
        c+=1
    else:
        yield a

f=fibonacci(10)

print("Start...")
for x in f:
    print(x, end=" ")
else:
    print("End.")

