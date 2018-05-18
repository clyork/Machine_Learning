#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 23:33:26 2018

@author: codyyork
"""
###data preprocessing###

##importing the libraries##

#math library
import numpy as np

#plot charts
import matplotlib.pyplot as plt

#import and manage datasets
import pandas as pd


dataset = pd.read_csv("/Users/codyyork/Documents/GitHub/Machine_Learning/Data Preprocessing/Data.csv")

#:means all col so :-1 means all but last col
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

##Splitting the dataset into Training and Testing##
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

##Taking care of missing data##
"""
#cmd + i brings up help menu
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN", strategy = 'mean', axis = 0)

#1:3 includes lower but ecludes higher so col 1 + 2 
#Col 1 and 2 contain missing data
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])
"""

##Encoding Catagorical Data ##
"""
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder 
LabelEncoder_x = LabelEncoder()
x[:, 0] = LabelEncoder_x.fit_transform(x[:, 0])

# Encoding the Dependent Variable
LabelEncoder_y = LabelEncoder()
y = LabelEncoder_y.fit_transform(y)

#dummy encoding 
from sklearn.preprocessing import OneHotEncoder
oneHotEncoder = OneHotEncoder(categorical_features = [0])
x = oneHotEncoder.fit_transform(x).toarray()
"""

##Feature Scaling##
"""
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
"""






















