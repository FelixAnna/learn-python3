#! /usr/bin/env python3

"""
This part shows you
How to run a Fibonacci function
"""

r={0:0,1:1}
a,b,index=0,1,2
while index<100:
    a,b=b,a+b;
    r[index]=b;
    index+=1;

for x in r.keys():
    print(r[x],end=',')
