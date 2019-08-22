#! /usr/bin/env python3

"""
This code shows you
how to use dict
in python3
"""

sa,sb={},{'name':'Felix', 'age':23, 100:'100%'}

print(sb[100]=='100%')

sa['name']='Anna'
sa['age']=23
sa[100]='80%'

print(sa['age']==23)

del sa[100]
sa.clear()

print(len(sb) ==3)
print(str(sb))
print(type(sb))

sc=sb.copy()
print(sc.keys())
print(sc.values())
print(sc.items())
sc.update({100:"90%"})
print(sc[100])
sc.pop(100)
print(sc.popitem())
sc.setdefault(99,0)
sc.setdefault('name','Unknown')
print(sc)

print(99 in sc)
for x in sc.items(): print(x)
