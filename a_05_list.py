#! /usr/bin/env python3

"""
This part contains common list
examples.
"""

l=["Hello","world",28,75.0]

print(l[0]=="Hello")
print(len(l[2:])==2)

l[2]=18;
print(l[2]==18)

del l[2]
print(len(l)==3)

print(len(l*3+l)==12)
print(75.0 in l)
print(18 not in l)

for x in l:
    print(x, end=" ")

l[1]=[1,2,3]
print(l[1]==[1,2,3])
print(l[1][0]==1)

print(max(l[1]))
print(min(l[1]))

b=list((1,3,5,7))
print(b)

b.append("hello")
print(b.count(1)==1)
print(b.count(4)==0)

b.extend((37,49))
b.extend([57,28])
print(len(b) == 9)
b.insert(1,2)
b.pop()
b.remove("hello")
b.reverse()
b.sort(key=None, reverse=True)

print(b)
b.clear()
print(len(b)==0)
c=l.copy()
print(c[0:])
