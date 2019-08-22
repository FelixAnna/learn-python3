#! /usr/bin/env python3

"""
This part domenstrator you
how to use set
in python3
"""

sa,sb,sc=set(),{1,2,3,4,5,6},set({3,5,7,8,9})

print(type(sa))
print(isinstance(sb, set))

print(3 in sb)
print(7 not in sb)

print(sb - sc == {1,2,4,6})
print(sb | sc == sb.union(sc) == {1,2,3,4,5,6,7,8,9})
print(sb & sc == sb.intersection(sc) == {3,5})
print(sb ^ sc == sb.symmetric_difference(sc) == {1,2,4,6,7,8,9})

sd={x for x in sb if x not in sc}
print(sd == {1,2,4,6})

sb.add(7)
sb.add("Hello")
sb.update((1,8,9))
sb.update({0,-1})
print(sb)

sb.remove("Hello")
sb.discard("noexists")
sb.discard(-1)
print(sb)

sb.pop()
print(len(sb)==9)
