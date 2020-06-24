#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:11:14 2020

@author: emrecelik
"""
# %% Variables
print("Variables")
integer = 10
day = "monday"
number = 10.1

# %% Built-in Functions
print("type(number):",type(number))
print("len(day):",len(day))

# %% User Defined Functions
print("\nUser Defined Functions")
def myFunc(var1, var2):
    """
    function study

    Returns
    -------
    (var1 + var2) / 2

    """
    return (var1 + var2) / 2

print("myFunc(100,50):",myFunc(100, 50))

# %% Default and Flexible Functions
print("\nDefault and Flexible Functions")
def circleRound(r, pi = 3.14):
    """
    Parameters
    ----------
    r : Number
        Radius.
    pi : TYPE, optional
        DESCRIPTION. The default is 3.14.

    Returns
    -------
    Number
        Circle Round.
    """
    return 2*pi*r

print("circleRound(2):",circleRound(2))


def calculate(x, y, *args):
    print(args)
    return x + y

print("calculate(1, 2, 3, 4, 5):",calculate(1, 2, 3, 4, 5))

# %% Lambda Functions
print("\nLambda Functions")
square = lambda x: x*x
print("square(2):",square(2))






