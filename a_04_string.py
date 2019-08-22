#! /usr/bin/env python3

"""
This part contains common string
examples
"""

a,b="Hello",'world!'

print(a[0]=='H')
print(b[1:2]=='o') #b[1,2)

c=a[:2]+' '+'is boy.'
print(c=="He is boy.")
print("I am \
a \
girl.");

print("""i am a 
boy.""")

print("\\a\'\"\a\b\n\000\v\t\r\f\o77 \xa0\other");

print(a+b=="Hello world")
print(a*2=="HelloHello")
print(a[1]=='e')
print('e' in a)
print('E' not in a)
print(r'\n'=='\\n')

print("H" == ("%c" %(a[0])))
print(b == ("%s" %(b)))
print("256" == ("%d" %(256)))
print("-256" == ("%u" %(-256)))
print("42" == ("%o" %(34)))

print("a" == ("%x" %(10)))
print("A" == ("%X" %(10)))
print("0010.89" == ("%07.2f" %(10.89)))
print("1.230000e+08 1.230000E+08" ==("%e %E" %(123000000,123000000)))  #6digit after point
print("1.23e+08 1.23E+08" == ("%g %G" %(123000000, 123000000))) #remove 0 after point

# print("%p" %(a))

astr, bstr="hh","hello world"
print(astr.upper() == "HH")
print("HH".lower() == astr)
print(bytes.decode(astr.encode()) == astr)
print(astr.capitalize() =="Hh")
print(astr.center(8,"*") == ("***%s***" % (astr)))
print(astr.endswith('h')==True)
print(astr.startswith('a') ==False)
print(len(astr.split("h")) == 3)
print(len(astr)==2)
print(bstr.title() == "Hello World")
print(bstr.swapcase() == "HELLO WORLD")
print(bstr.replace("world", "Felix")=="hello Felix")
print(astr.isupper() == False)
print(astr.istitle()==False)
print(astr.islower())
print(bstr.index("w")==6)
print(astr.isalnum())
print(bstr.swapcase)

print("{0} {1} {0}.".format("hello",365))
print("Your name:{name}, your weight: {weight}".format(name="Felix",weight="75kg"))

user={"name":"Felix","age":23}
print("your name:{name}, your age:{age}".format(**user))
attributes=["SDE",".net",35000]
print("Your title is {0[0]},your skill is {0[1]}, your salary is {0[2]:.2f} per month.".format(attributes))
