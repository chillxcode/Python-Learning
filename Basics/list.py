#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 23:16:14 2020

@author: emrecelik
"""
# %% Lists
print("Lists")
list_int = [1, 2, 3, 4, 5]
print("type(list_int):",type(list_int))
print("list_int[last]:",list_int[-1])
list_str = ["a", "b", "c", "d", "e"]
print("type(list_str):",type(list_str))
print("list_str[last]:", list_str[-1])

# dir(list_int)
# =============================================================================
# Out[40]: 
# ['__add__',
#  '__class__',
#  '__contains__',
#  '__delattr__',
#  '__delitem__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__getitem__',
#  '__gt__',
#  '__hash__',
#  '__iadd__',
#  '__imul__',
#  '__init__',
#  '__init_subclass__',
#  '__iter__',
#  '__le__',
#  '__len__',
#  '__lt__',
#  '__mul__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__reversed__',
#  '__rmul__',
#  '__setattr__',
#  '__setitem__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  'append',
#  'clear',
#  'copy',
#  'count',
#  'extend',
#  'index',
#  'insert',
#  'pop',
#  'remove',
#  'reverse',
#  'sort']
# =============================================================================

# help(list_int.append)
# =============================================================================
# Help on built-in function append:
# 
# append(object, /) method of builtins.list instance
#     Append object to the end of the list.
# =============================================================================

# %% Tuples
print("\nTuples")
t = (1, 2, 3, 3, 4, 5)
print("tuple same value count:",t.count(3))

# %% Dictionary
print("\nDictionary")
dictionary = {"a":1,
              "b":2,
              "c":3}

print("dictionary['a']",dictionary["a"])

