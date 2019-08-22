#! /usr/bin/env python3

"""
Try use the package we define in
a_18_package.py
"""

import a_18_package

print(dir())

print('base' not in dir())

#we'd better use this way
from a_18_package import base
print(a_18_package.base.base())

#or use this way
from a_18_package import *
print(a_18_package.base.other())
print(dir())

from a_18_package.math import basic,high_level
print(dir())
print(basic.add(1,2) == 3)
print(high_level.divide(18, 3) == 6)

#we have initialized __all__ insides, song is excluded
from a_18_package.history import *
print(tang.length())
print('song' not in dir())

#import explicted
from a_18_package.history import tang,song
print('song' in dir())
print(song.creator())
