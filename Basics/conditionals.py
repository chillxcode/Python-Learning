#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 23:46:25 2020

@author: emrecelik
"""
# %%Conditionals
print("Conditionals")
var1 = 10
var2 = 10

if(var1 > var2):
    print("var1 > var2")
elif(var1 == var2):
    print("var1 == var2")
else:
    print("var1 < var2")

l = [1, 2, 3, 4, 5]
value = 3
if value in l:          # this is also work with dict
    print("yes, {} is inside the list".format(value))
else:
    print("no")

# %% For Loops
for each in range(11):
    print("each:",each)
    
# %% While Loops
i = 0
while(i < 4):
    print("i:",i)
    i += 1