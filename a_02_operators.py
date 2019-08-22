#! /usr/bin/env python3

'''
This file contains common operator examples
'''

a,b,c,d=1,2,3,4

if a>d:
    print("a>d")
elif a<b:
    print("a<b")
else:
    print("a between b and d")

a+=b;
a-=b;
a*=b;
a/=b;

print(a==1);

b**=c;
print(2==b%c);

b//=c;
print(2==b);

a=53  #0011 0101
b=108 #0110 1100

print(a|b==125)  #0111 1101
print(a&b==36)   #0010 0100
print(a^b==89)   #0101 1001
print(~a==-54)   #1100 1010
print(a<<2==212) #1101 0100
print(a>>2==13)  #0000 1101

print(a==53 and b>100);
print(a<100 or b<100);

print(a in [1,22,53,29]);
print(a not in (1,22,52,29));

e=a;

print(e is a)

f=53;
print(f is a);

a=b="hello"
c="hello"
print(a is b)
print(a is c)
