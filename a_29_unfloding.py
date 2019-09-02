#! /usr/bin/env python3

"""
calculate paper folding problem
"""
class Paper:

    l=w=h=0;
    def __init__(self, l, w, h):
        self.l=l;
        self.w=w;
        self.h=h;
    def fold(self):
        if self.h>self.l/2 and self.h>self.w/2:
            print("Can not fold any more.")
            raise Exception("Can not fold any more.")
        elif self.l>self.w:
            self.l=self.l/2
            self.h=self.h*2
            print("divide long")
        else:
            self.w=self.w/2
            self.h=self.h*2
            print("divide width")
    def print(self,i):
        print("folded/unfolded {0} times, long={1:E}, width={2:e}, height={3:E}".format(i, self.l,self.w,self.h))
    def unfold(self):
        if self.h<=1E-30:
            print("Too samll to unfold any more.")
            raise Exception("Can not unfold any more.")
        elif self.l<self.w:
            self.l*=2
            self.h/=2
        else:
            self.w*=2
            self.h/=2



l=float(input("please input long:"))
w=float(input("please input width:"))
h=float(input("please input height:"))

pa=Paper(l,w,h)

pb=Paper(1,1,1)

try:
    for i in range(100):
        pa.fold()
        pa.print(i+1)
    else:
        print("done {} times".format(i))
except Exception as ex:
    print(repr(ex))
else:
    print("done {} times".format(i))


try:
    for i in range(100):
        pb.unfold()
        pb.print(i+1)
    else:
        print("done {} times".format(i))
except Exception as ex:
    print(repr(ex))
else:
    print("done {} times".format(i))
