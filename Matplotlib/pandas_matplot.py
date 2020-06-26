#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:51:42 2020

@author: emrecelik
"""

import pandas as pd

df = pd.read_csv("iris.csv")

print("Columns:\n\n", df.columns)

print("\nUnique Species:\n", df.Species.unique())

print("\nInfo:\n")
print(df.info())

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]

print("\nSetosa:\n")
print(setosa.describe())

print("\nVersicolor:\n")
print(versicolor.describe())

# %% LINE PLOT
import matplotlib.pyplot as plt

df1 = df.drop(["Id"], axis = 1)

# df1.plot(grid = True, alpha = 0.5)
# plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label= "setosa")
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label= "versicolor")
plt.plot(virginica.Id,virginica.PetalLengthCm,color="blue",label= "virginica")
plt.legend()
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.show()

# %% SCATTER PLOT

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]


plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color="red",label="setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm,color="green",label="versicolor")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color="blue",label="virginica")
plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("scatter plot")
plt.show()

# %% HISTOGRAM

plt.hist(setosa.PetalLengthCm,bins= 50)
plt.xlabel("PetalLengthCm values")
plt.ylabel("frekans")
plt.title("hist")
plt.show()

# %% BAR PLOT
import numpy as np

x = np.array([1,2,3,4,5,6,7])
a = ["a","b","c","d","e","f","g"]
y = x*2+5

plt.bar(a,y)
plt.title("bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# %% SUBPLOTS

df1.plot(grid=True,alpha= 0.9,subplots = True)
plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.subplot(2,1,1)
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label= "setosa")
plt.ylabel("setosa -PetalLengthCm")
plt.subplot(2,1,2)
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label= "versicolor")
plt.ylabel("versicolor -PetalLengthCm")
plt.show()












