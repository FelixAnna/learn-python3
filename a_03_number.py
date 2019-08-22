#! /usr/bin/env python3

"""
This part contains common number and math function pratice
@2019-08-15
"""

a=1;b=2;c=a/b;d=0x12;

del a,b,c,d;

a,b,c,d=1,2.01,0x16,3+2j;

print(isinstance(a,int))
print(isinstance(b,float))
print(isinstance(d,complex))
print(c==22)

print(22.0==float(c))
print(2==int(b))
print(c/b<11)

print(b**c>2**c)

from math import *
print(abs(-10)==10)
print(ceil(-10.1)==-10)
print(exp(3)>8)
print(fabs(-10)==10.0)
print(floor(-10.1)==-11)
print(log(8,2)==3)
print(log10(100)==2)
print(max(23,1,34,17)==34)
print(min(23,1,34,17)==1)
print(pow(2,6)==64)
print(sqrt(9)==3)
print(round(4.49)==4)

print(cos(pi/2)<0.00000000001)
print(sin(pi/2)==1)
print(tan(pi/4)>0.99999999999)

print(degrees(pi/2)==90)
print(radians(90)==pi/2)


