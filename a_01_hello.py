#! /usr/bin/env python3

'''
test 
cdd
'''

c=1;
d=2;

# this is some comments
# 资料发现需

print(c + d);
print(c+d);

a="hello";
b="23w查询资料发现需要重新编译安装wwadap";

print(a + b);

if d>2:
    print("C is bigger than 2");
else:
    print("C is smaller than 2");

e= c + \
        d;

print(e);
#define a list
numbers=[1,3,4,2,5,6,7,8,9];
names=[r"\rabc","d\nef",'\nighi'];


print(names[1:2]);
print(numbers[2:5]);

test_str=('''heelo
itr f=a+b;
        this
        is me.''');
print(test_str);
half=c/d;
print(half);
input("\n\ninput anything to continue...");

import sys;
x='felix';
sys.stdout.write(x+'\n\n');

if d>3:
    print("3+");
elif d>1:
    print("1~2");
else:
    print("0-");

loop=9;
while loop>0:
    print(loop, end="");
    print(",", end="");
    loop=loop-1;

print();

import sys;
for i in numbers:
    print(i);


from sys import path;

print(path);

salary=2999999.98;
print(salary);

a, b, c, e,f, g=2,99.8,"hello",True,[23,46,25], (4,5,7);

check=isinstance(b,float);
print(check);

print(b**a);

print(b//a);

print(c[0:3]);
print(c*3);

f[0]=11;
f=f+[98,76];
print(f[0:5]);
print(f[-1::-1]);
print(f[5::-1]);
print(g[0:]);
del a,b,c,d,e,f,g;

h,i,j={'Felix','Johan','Tom','Ashraf','Tom'},set('felix'),set('ashraf');

print(h);
print(i&j);
print(i-j);
print(i|j);

k,l={},{1:"Felix","a":"A",0:23};

print(l[1]);
print(l[0]);
print(l["a"]);

k[23]="46";
print(k[23]);

l={x:x**3 for x in (1,2,3,4,5,6,7,8,9,10,11,12,13)};
        
print(k.keys());
print(k.values());

x="399";
y=int(x,base=10);
z=str(x);
l=list(z);
k=set(l);
x=float("399")

print(isinstance(x, int))
print(isinstance(x, float))

a,b=55,'str'
x=();
x=(a,)
print(isinstance(x, tuple))

x={}
print(isinstance(x, dict))
x="395";
y=int(x,base=10);
x={a,b}
print(isinstance(x, set))
x={a:b}
print(isinstance(x,dict))
print(eval('13*y'));
print(k);
