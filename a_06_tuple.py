#! /usr/bin/env python3

"""
This part will show you
How to use tuple
in Python3+
"""

ta=('google','baidu','bing.com')
tb=1,2,3,4

print(isinstance(tb, tuple))
print(type(ta))

tc=()
tc=(36,)
print(isinstance(tc, tuple))

print(ta[0]=='google')
print(tb[1:3]==(2,3))

print(ta+tb)
print(ta*3)

del ta;
#print(ta) #not defined

print(3 in tb)
print(10 not in tb)

for x in tb:
    print(x,end=",")

print(max(tb)==4)
print(min(tb)==1)
print(tuple([1,3,4]) == (1,3,4))



