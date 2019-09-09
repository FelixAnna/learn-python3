#! /usr/bin/env python3

"""
This part shows you
json.dumps(data[,f]): dump obj to json;
json.loads(json_str): load and convert josn str to obj.
"""

di={"name":"felix","age":20}

import json

jstr=json.dumps(di)
print("json_str: {}".format(repr(jstr)))

di2=json.loads(jstr)
print("dict: {}".format(repr(jstr)))

class test(json.JSONEncoder):
    def __init__(self, a, b, c):
        self.A=a
        self.bB=b
        self.Cc=c
    def toJson(self):
        return json.dumps(self, default=lambda o:o.__dict__,sort_keys=True, indent=4)

ti=test(1,"felix",36000)
ti2=test(2,"felix yu", 450000)

print(ti.toJson())
print(json.loads(ti2.toJson()))

