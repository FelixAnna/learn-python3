#! /usr/bin/env python3

"""
This part review basic python sequence types:
list, tuple, dict, set
"""

a, b=[1, 2, 3], (4, 5, 6)

print(isinstance(a, list))
print(isinstance(b, tuple))

#use as stack
a.append(4) #[1,2,3,4]
c=a.pop()   #[1,2,3]
print(c==4)
print(a.index(3)==2)

a.remove(2) #[1,3]
a.reverse() #[3,1]
print(a.index(3)==0)

a.extend(b) #[3,1,4,5,6]
print(len(a)==5)


#example of use a queue
from collections import deque
queue = deque(a)
queue.append(7) #[3,1,4,5,6,7]
queue.popleft() #[1,4,5,6,7]
print(len(queue)==5)

#example of use stream way
c=[x**2 for x in a if x%2==1]
print(isinstance(c, list))

d=tuple(c)
print(isinstance(d, tuple))

#reverse a[row=5*col=4]
a=[[4,5,5,6],[11,13,15,3],[21,15,9,7],[19,18,78,6],[-1,9,98,102]]
e=[[x[i] for x in a] for i in range(4)] #e is [col=5*row=4]
print(len(e)==4)

#nested list
a=[[x,x**2] for x in range(100)]
print(len(a)==100)

#test del part
del a[1:99]
print(len(a)==2)

del a
print('a' not in vars())

#tuple
b='Hello','There','!'
print(isinstance(b, tuple))
print('!' in b)
print('?' not in b)

c='onlyone',b,(3,4,5,5,6)
print(len(c)==3)

#set
a,b,c=set(),{1,2,3},{2,3,4}
print(len(b|c) == 4)
print(len(b&c)==2)
print(len(b^c)==2)
a=[x**2 for x in b|c]
print(a)
print(len(a)==4 and a[3] == 16)

#dict
a, b, c, d={}, {'name':'felix', 'age':23}, \
        dict([('name','felix'),('age',23)]), \
        dict(name='Felix', age=23)
print(sorted(b.keys()) == sorted(c.keys()))
del b['age']
print('age' not in b)
print('name' in b)
for k,v in c.items():
    print(k,v)

#loop 2+
a,b=['Felix','Anna'],[18,19]
for x,v in zip(a,b):
    print(x,v)

