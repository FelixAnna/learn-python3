#! /usr/bin/env python3

"""
This part show you
How to user iterator
How to define Iterator
"""

a,b=[1,2,3],(4,5,6)

ai, bi=iter(a), iter(b)

for x in ai:
    print(x, end=",")

print()

while True:
    try:
        print(next(bi))
    except StopIteration:
        print("Done")
        break;

#define a iterator class
class MyIterTest:
    def __iter__(self):
        self.value=1
        return self
    
    def __next__(self):
        if self.value<=3:
            x,self.value=self.value,self.value+1
            return x
        else:
            raise StopIteration


my_iter = MyIterTest()
myi=iter(my_iter)

print(next(myi))
print(next(myi))
print(next(myi))
print(next(myi))
print(next(myi))
print(next(myi))
print(next(myi))
print(next(myi))







