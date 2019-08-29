#! /usr/bin/env python3

"""
This part shows you how to use:
    re.complie(...)  
    re.match(pattern, string, flags=0)
    re.match(string, flags=0)
    re.search(partten, string, flags=0)
    re.findall(partten, string, pos=0, endpos=len(string))
    re.findall(string, pos=0,endpos=len(string))
    re.finditer(.....)
    re.sub(partten, repl,string, count=0, flags=0)
    
    re flags
    re partten
"""

import re

pw3=r"w{3}"
pb=r"(abc)+ [0-9a-zA-Z]"

w3ba="www.ba.com"
baw3="ba.www.com"
mw3="ba.www.comwww.cn"
#match : match partten from the start
rew3=re.compile(pw3)
print(rew3.match(w3ba))
print(rew3.match(baw3))
print(re.match(pw3, w3ba))

#search : find the first match value, not need from start
print(re.search(pw3, baw3))
print(rew3.search(baw3))

#sub : find matches and replace them
print(re.sub(pw3, "v3", mw3))
print(re.sub(pw3, "v3", mw3,1))

#findall : find all matches
print(rew3.findall(mw3))
print(rew3.findall(mw3, 4,len(mw3)))

#finditer : find for iter
for i in rew3.finditer(mw3):
    print(i)
    print(i.group())
    print(i.span())
    print(i.start())
    print(i.end())

#split
print(rew3.split(w3ba))

#flags
print(re.search("WWw",w3ba, re.I)) #re.I : case in sensitive
print(re.findall(r"^A[\s\S]+z$", """a little biz
aas size.
a sasds z""",re.M|re.I)) #re.M search in multiple lines

#partten
print(re.findall("\s+","www a   \n\rbc.com.")) #\s: match space [\r\n\t\f]
print(re.findall("\S+","www a   \n\rbc.com.")) #\S: not \s
print(re.findall("\d+","he is 32 years old")) #\d: any digit
print(re.findall("\D+","he is 32 years old")) #\D: not \d
print(re.match("\Aabc\Z","abc")) #\A \Z\z = ^ $
print(re.match("\w+", "aA_9 he\n")) #\w: match digit + alpha + _
print(re.match("\W+", "aA_9 he\n")) #\W: not \w
#....[^a-z] = not a-z 
#....\b = binder of world and space: er\b matcher never
print(re.findall("er\B","never")) #....\B = not \b : er\B not matcher never but can match there
print(re.findall("er\B","there"))
print(re.findall(r"er\b","never"))
print(re.findall(r"er\b","there"))
print(re.findall("[^a-z]+","aboy 123 years old."))
