#! /usr/bin/env python3

"""
This part shows you:
    How to define a class;
    How to define public attrs, methods
    How to define private attrs,methods;
    How to drive calss, classes;
    How to call supper class methods (constructor);
    How to override methods;
    how to overload operators.
"""

class creature:
    name = ''
    age = 0
    weight=0 
    __grade =0 #start with __ means the attrs is private
    def __init__(self, n, a):
        self.name=n
        self.age=a

    def assign(self, w):
        print("assign in creature")
        self.weight=w
        self.__assigngrade(w**2)
    def __assigngrade(self,g):#start with __ means private methods
        self.__grade=g
        

    def print(self):
        print("Creature name={}, age={}, weight={}.grade={}.".format(self.name,self.age,self.weight,self.__grade))

class people(creature):
    def __init__(self, n, a, w):
        creature.__init__(self,n,a)
        self.assign(w)
    
    def assign(self, w):  #overwride creature.assign(self,w)
        print("assign in people")
        self.weight=w

    def single(self):       #new public method
        print("la la la ....")

class cat(creature):
    color="red"
    def __init__(self,n,a,w,c):
        creature.__init__(self,n,a)
        self.assign(w)
        color=c
    def assign(self,w): #overwride creature.assign(self,w)
        print("assign in cat")
        self.weight=w

    def speak(self):
        print("miao, miao, miao")

class pecat(cat, people): #methods in cat have high priority
    def __init__(self, n, a, w, c):
        cat.__init__(self,n,a,w,c)
        people.__init__(self,n,a,w)
    def print(self):  #override creature.print(self) method
        print("pecat name={},age={},weight={},color={}".format(self.name,self.age,self.weight,self.color))
n,a,w,c="Sam",6,18,"White"
animinal = pecat(n,a,w,c)

#call cat assign
animinal.assign(16)
animinal.speak()
animinal.single()
animinal.print() #pecat.print(self)

super(pecat, animinal).assign(15)  #cat->people->create.assign(self,w)
super(pecat, animinal).print() #cat->people->creature.print(self)

ct=creature(n,a)
ct.assign(14)
ct.print()
#ct.__grade
#ct.__assigngrade(10)
#super(people, super(pecat, animinal)).print()
