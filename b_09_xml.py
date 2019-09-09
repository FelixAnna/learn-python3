#! /usr/env/bin python3

"""
This part shows you
how to parse xml by dom
dom will parse the xml 
"""

import xml.dom.minidom

path="./movies.xml"
collectionTree=xml.dom.minidom.parse(path)

collection=collectionTree.documentElement
if collection.hasAttribute("no"):
    print("Root shelf no  is: {}".format(collection.getAttribute("no")))

movies=collection.getElementsByTagName("movie")

for m in movies:
    print("....movies....")
    if m.hasAttribute("title"):
        print("Title is: {}".format(m.getAttribute("title")))

    size=m.getElementsByTagName("size")[0]
    print("Size is: {}".format(size.childNodes[0].data))
    
    date=m.getElementsByTagName("date")[0]
    print("Date is: {}".format(date.childNodes[0].data))
    rating=m.getElementsByTagName("rating")[0]
    print("Rating is: {}".format(rating.childNodes[0].data))


