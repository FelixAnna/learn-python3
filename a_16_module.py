#! /usr/bin/env python3

"""
This part show you
How to define and use module
"""

if __name__ == '__main__':
    print("constructor run")
else:
    print("imported")

def fib(n):
    i,j, index=0,1,0
    while index<n:
        i, j=j,i+j
        index+=1
    else:
        return i

def times(n,m):
    return n**m

pi=3.1415926
days_in_year=365
