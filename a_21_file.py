#! /usr/bin/env python3

"""
This part show you common
file function members
"""

path="/home/yuxiangyong/dev/temp/file.txt"
fa=open(path, 'w+')

fa.write("Hello world")
fa.writelines({"\nXiangyong","\nAnna","\nJiahang","\nQian"}) #param is sequence - list/tuple/set/dict

fa.close()

with open(path, 'r+') as fb:
    line=fb.readline()
    lines=fb.readlines()
    content = fb.read()

    print(line)
    print(lines)
    print(content)
    
    
    print(fb.tell())
    fb.seek(0,0)
    print(fb.tell())
    fb.truncate()
    print(fb.read())
    fb.writelines((str(1),repr(2),"3"))
    fb.flush()
    fb.close
# not use a/a+ here for the pointer is at end.
with open(path, 'r+') as fc:
    content = fc.read()
    print(content)
    print("content is: {}".format(content))

