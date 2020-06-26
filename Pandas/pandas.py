#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 22:43:36 2020

@author: emrecelik
"""

# 1) Fast and effective for dataframes
# 2) CSV and Text files usage is easy
# 3) Missing data handling
# 4) Reshape, Slicing, Indexing is easier
# 5) Useful for timeseries data analysis

import pandas as pd

dictionary = {"NAME":  ["emre", "sude", "emel", "can"],
              "AGE":   [23    , 22    , 19    , 21],
              "SALARY":[100   , 150   , 200   , 250]}

dataFrame = pd.DataFrame(dictionary)

head = dataFrame.head(3)    # First 3 item
tail = dataFrame.tail(3)    # Last 3 item


# %% Basic Methods

print(dataFrame.columns)

print(dataFrame.info())

print(dataFrame.dtypes)

print(dataFrame.describe()) #numeric feature = columns (age,salary)


# %% Indexing and Slicing

print(dataFrame["NAME"])    # Print Column
print(dataFrame.NAME)       # Same Thing
print(dataFrame.iloc[:, 0]) # Print 0 index column

dataFrame["GENDER"] = ["male", "female", "female", "male"]   # Adding new feature (column)

print(dataFrame.loc[:2, "AGE"]) #First 3 Row in Age column

print(dataFrame.loc[:2, "AGE":"GENDER"])

print(dataFrame.loc[:2, ["NAME", "SALARY"]])    ##First 3 Row with specific column


# %% Filtering

filter1 = dataFrame.SALARY > 150
filteredData = dataFrame[filter1]

filter2 = dataFrame.AGE < 20

filteredData2 = dataFrame[filter1 & filter2]


# %% List Comprehension

# import numpy as np
# mean_np = np.mean(dataFrame.SALARY)

mean = dataFrame.SALARY.mean()

# depends on salary average, adds new column to dataframe high or low
dataFrame["SALARY_LEVEL"] = ["low" if mean > each else "high" for each in dataFrame.SALARY]

# lower character to columns data
dataFrame.columns = [each.lower() for each in dataFrame.columns]

# if cell has " " character, this code makes " " -> "_"
dataFrame.columns = [each.split()[0] + "_" + each.split()[1] if len(each.split()) > 1 else each for each in dataFrame.columns] 


# %% Drop and Concatenating

# deletes column, axis = 1 in columns, axis = 0 is row, inplace = True is edit changes to real dataFrame
dataFrame.drop(["GENDER"],axis = 1, inplace = True)

data1 = dataFrame.head()
data2 = dataFrame.tail()

vertical = pd.concat([data1, data2],axis = 0)

horizontal = pd.concat([data1, data2], axis = 1)


# %% Transforming Data

dataFrame["list_comp"] = [each * 2 for each in dataFrame.age]

def multiply(age):
    return age*2

dataFrame["apply_method"] = dataFrame.age.apply(multiply)






