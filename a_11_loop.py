#! /usr/bin/env python3

"""
This part show you:
How to use for loop;
How to use while loop;
How to use else with loop;
How to use break, continue, pass with for/while loop;
How to use range(x)/range(start,end,step) with for loop.
"""

a,b=0,10
for x in [a,b]:
    if x==b:
        print(x);
    else:
        print(a,end=',')
else:
    print("Loop exited: no more element in list [{first}, {last}]".format(first=a,last=b))
while a<=b:
    if a==b:
        print(a);
    else:
        print(a, end=',')
    a+=1;
else:
    print("Loop exited: %d is now bigger than %d" % (a,b))

for x in range(b):
    if x==b-1:
        print(x)
    else:
        print(x, end=',')

c=["C#","Java","Python","Go","C++","C","React","JavaScripts"]
for x in range(len(c)):
    if c[x] == "C#":
        print("I Know {}".format(c[x]));
    elif c[x] == "Go":
        print("Skip {0}".format(c[x]))
        continue
    elif c[x] == "JavaScripts":
        print("Break %s" % (c[x]))
        break;
    else:
        print("Pass {lang}".format(lang=c[x]))
        pass

while True:
    val=str(input("Please input something (exit for end):"))
    if val == 'exit':
        print("End.")
        break
    else:
        print(val)

