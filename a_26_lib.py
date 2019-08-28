#! /usr/bin/env python3

"""
This part shows you common libriay usage:
    os for operator system related functions;
    dir(..), help(...) for find help documents;
    shutil for file and folder common management;
    glob for search files in a folder;
    sys for commandline argv access,redirect output with stdin,stdout,stderr, and exit program;
    re for regular expression functionalites;
    math for common float calculation;
    random for random genrator related;
    urllib.request for access internet;
    smtplib for send email;
    datetime for date and time operations;
    zlib, gzip, bz2, zipfile,tarfile for compression and de-compression;
    timeit for valuation the cost;
    doctest for test according to inline code;
    unittest for unit test.
"""

#os 
import os

path = os.getcwd()
fa="./ignoreme/test.txt"
fb=fa.replace("txt","log")
os.system("mkdir ignoreme")
with open(fa,"w+") as fw:
    fw.write(path)


#dir(lib), help(lib)
##dir(os)
##help(os)

#shutil
import shutil

shutil.copyfile(fa,fb)
shutil.move(fa,fb.replace("log","md"))

#glob
import glob
files=glob.glob('*.py')
print(repr(files))

#sys
import sys
print(sys.argv)
'''print(sys.stdin.read(33))'''
sys.stdout.write("out msg\n")
sys.stderr.write("out error\n")

#re
import re
print(re.findall(r'\by[a-z0-9]*', 'I am yujianghang, song of yuxiangyong'))

#math
import math
print(math.sin(math.pi/2) == 1 and True)

#random
import random
print(random.choice((1,2,3)))
print(random.randrange(100))
print(random.random())
print(random.sample(range(1000),10))

#urllib.request
from urllib.request import urlopen

baidupage=""
for line in urlopen('http://www.baidu.com'):
    line=line.decode('utf-8') #decode the binary data to text
    if 'baidu' in line or 'Baidu' in line:
        print(line)

    baidupage+=line
else:
    print("Loop exited.")

#smtplib
import smtplib

''' #need smtp in localhost
server =smtplib.SMTP('localhost')
server.sendmail("a@example.com","b@example.com","something")
server.quit()
'''

#datetime
import datetime
today=datetime.date.today()
tommorrow=today+datetime.timedelta(days=1)
birthday=datetime.date(1989,5,26)
print(tommorrow)
print(tommorrow.strftime("%y-%m-%d = %Y %b %d = %Y %B %d"))
print((today-birthday).days)

#zlib, gzip, bz2,zipfile, tarfile
import zlib
baidubytes=bytes(baidupage, 'utf-8')
print("before compress: ", len(baidubytes))
print("after compress: ", len(zlib.compress(baidubytes)))

#timeit
from timeit import Timer
print(Timer('t=a; a=b; b=t','a=1;b=2').timeit())
print(Timer('a,b=b,a','a=1;b=2').timeit())

#doctest
def addall(a,b):
    "we will add a and b"
    if a==0:
        raise IOError()
    return a+b

import doctest
doctest.testmod()

import unittest

class testaddal(unittest.TestCase):
    def test_addall(self):
        self.assertEqual(addall(1,2),3)
        self.assertRaises(IOError, addall, 0,3)

unittest.main()

os.system("rm -rf ignoreme")
sys.exit()
