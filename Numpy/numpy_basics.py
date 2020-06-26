#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 20:02:54 2020

@author: emrecelik
"""
import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print("array.shape:", array.shape)

matrix = array.reshape(3, 4)

print("matrix:\n", matrix)
print("matrix.shape:", matrix.shape)
print("matrix.dimension:", matrix.ndim)

print("matrix data type:", matrix.dtype.name)
print("matrix.size:", matrix.size)

zeros = np.zeros((3,4))
zeros[0,0] = 3
print(zeros)

inOrder = np.arange(10, 50, 10)
print("inOrder: ", inOrder)

inSpace = np.linspace(10, 50, 10)
print(inSpace)

# %% Numpy Basic Operations

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
print(a ** 2)

print(np.sin(a))

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[3, 2, 1], [6, 5, 4]])

print("\na * b:\n", a * b)

print("\ndot multiply:\n", a.dot(b.T))

rn = np.random.random((5, 5))
print("\nrandom:\n", rn)
print(rn.sum())
print(rn.max())
print(rn.min())

print("\nsqrt:\n", np.sqrt(rn))
print("\nsquare:\n", np.square(rn))

print("row+:   ", rn.sum(axis=0))
print("column+:", rn.sum(axis=1))

# %% Indexing and Slicing

array = np.array([1, 2, 3, 4, 5, 6, 7])
print("\narray:\n", array)

print("\nslice:", array[0:3])

print("\nreverse:\n", array[::-1])

array1 = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print("\narray1:\n", array1)
print("\nslice:\n", array1[1,1:4])

# %% Shape Manipulation

array = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print("\narray:\n", array)

# flatten
a = array.ravel()
print("\na:", a)

array2 = a.reshape(3,3) # resize
print("\nreshape(3,3):\n", array2)

arrayT = array2.T
print("\narrayT:\n", arrayT)

# %% Stacking array

array1 = np.array([[1, 2],[3, 4]])
print("\narray1:",array1)
array2 = np.array([[-1, -2],[-3, -4]])
print("\narray2:",array2)

# Vertical
# array([[1, 2],
#        [3, 4]])
# array([[-1, -2],
#        [-3, -4]])
print("\nVertical:\n",np.vstack((array1, array2)))


# Horizontal
# array([[1, 2], [-1, -2],
       # [3, 4], [-3, -4]])
print("\nHorizontal:\n", np.hstack((array1, array2)))

# %% Convert and Copy

list1 = [1, 2, 3, 4]

npArray = np.array(list1)

list2 = list(npArray)

# np.array is a reference type
a = npArray.copy()  















