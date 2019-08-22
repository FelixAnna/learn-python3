#! /usr/bin/env python3

"""
This part shows
How to define function
How to use function
Parameter: need/optional/*tuple/**dict/named
Scope: local/global/nonlocal - vars()/locals()/globals()
Return/no-return values
lambda
"""

#define function without return
def no_return():
    print("no return")

no_return()


#define function with parameters
def param_fun(name, age, *score):
    print(name,' ', age, ':', score)

def param_fun_default(identity, salary=1000000):
    print("%s's salary is %.2f" % (identity, salary))

def param_fun_special(school, *, address):
    print("{0} at {1}".format(school, address))

def param_fun_dict(school, **students):
    print(students, " belongs ", school)

param_fun('Felix', 23, 88,99,78)
param_fun('Jiahang', 5)

param_fun_default(identity='felix', salary=450000)
param_fun_default('anna')

param_fun_special('Yonghe', address="Henan")
param_fun_dict("Yonghe", felix=23, jiahang=5)

#lambda examples
times=lambda x,y:x**y
plus=lambda x,y:x*y

print(2**4 == times(2,4))
print(2*4 == plus(2,4))

#global var for use global variable
#non-local var for use enclosing variable
value=1
def scope_fun(i):
    global value
    value+=i
    def inner_scope_fun():
        nonlocal i
        global value
        print(i," ",value)
    inner_scope_fun()
    
    i+=1
    if i<10:
        scope_fun(i)

scope_fun(3)

#if/else, try/except, for/while dont create new scope
def scope_iforlooportryexcept():
    a=1
    if True:
        b=2
    
    try:
        c=3
    except:
        d=4

    for x in range(3):
        e=5
        break;

    while True:
        f=6
        break;

    print(a==1 and b==2 and c==3 and e==5 and f==6)
    print('d' not in vars())
    print('c' in vars())
    print(vars())
    print(locals())
    print('g' in globals())

g=7
scope_iforlooportryexcept()
