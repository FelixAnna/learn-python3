#! /usr/bin/env python3

"""
This part will show you:
read input from commandline
str.format(...) usage
str % (...) usage
str(), repr(), rjust,ljust(),center(),zfill() usage
file read
file write
file.tell(),file.seek(,0|1|2) usage
with xx as file: usage
pickle dump/load usage
"""

#import sys
#print(sys.path)
#print(vars(sys))

#input usage
val=input("Please input a value:")
print("The value you have just inputed is: %s" % (val))

#old string format way
name, score='Felix', 96
print("Your name is: %s, your score is %3.1f" % (name,score))

#new str.format(...), !r means use repr(...), otherwise use str(...) = !s
print("Your name is: {!r}, your score is {}".format(name,score))
print("Your name is: {1}, your score is {0:3.1f}".format(score, name))
print("Your name is: {name}, your score is {score:3.1f}".format(score=score, name=name))

#str.format(dict), str.format(**dict)
stu={'Name':name, 'Score':score}
print("Your name is: {0[Name]}, your score is {0[Score]:3.1f}".format(stu))
print("Your name is: {Name}, your score is {Score:3.2f}".format(**stu))

stu={"Felix":score}
for name, score in stu.items():
    print("Your name is: {0}, your score is {1:3.2f}".format(name, score))


print(str(stu), end=' ');
print(repr(stu))

val='123'
print(str(val))
print(repr(val))
print(val.zfill(5))
for x in range(1,10):
    print("{0:2d} {1:3d} {2:4d}".format(x,x**2,x**3))

#open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#file append (create if not exist) -- a, a+ = a+ read
fpath='/home/yuxiangyong/dev/temp/test.txt'
fa=open(fpath, 'w+') #--a+
fa.write("Hello\n this is second line.\n End.")
fa.close()

#file read, r+ = r + write
fr=open(fpath, 'r+')
content = fr.read()
print(content)
for line in fr.readlines():
    print(line)

for line in fr:
    print(line)
fr.close()

#file write (create if not exists) -- w, w+ = w + read
with open(fpath, 'w+') as f:
    str=f.readline()   #read one line
    print(f)

    f.seek(10)
    f.write("I am here")
    #f.seek(2)
    f.write("second")
    #f.seek(-2, 2)
    f.write("last")

class hello:
    def __init__(self):
        self.value=123,
        self.name='Johan'

    def initial(self, na, val):
        self.name=na
        self.value=val

import pickle
test=hello()
test.initial("Felix",88)
with open(fpath, 'wb') as fwb:
    pickle.dump(test, fwb, -1) #dump object to file with the highest protocol available

with open(fpath, 'rb') as frb:
    newtest=pickle.load(frb) #load from dump file and de-serilize to newtest
    print(newtest.name, newtest.value)
        
