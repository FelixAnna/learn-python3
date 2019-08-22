#! /usr/bin/env python3

"""
This part have if-elif-else
Examples
"""
print('Start:')
a=1
while a<9:
    if a%3==0:
        print(a, "is times of 3")
    elif a%3==1:
        print("{0} is times of 3 plus {1}".format(a, 1))
    else:
        print("%d is times of 3 plus %d" % (a, 2))
    a+=1;
print('End.')
