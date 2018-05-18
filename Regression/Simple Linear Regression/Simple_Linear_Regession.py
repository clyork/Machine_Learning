#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 01:45:18 2018

@author: codyyork
"""
###Simple Linear Regression###

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("/Users/codyyork/Documents/GitHub/Machine_Learning/Regression/Simple Linear Regression/Salary_Data.csv")

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3)

##Fitting Simple Linear Regression to the Training Set##
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

##Predicting the Test set results##
y_pred = regressor.predict(x_test)
y_pred_training = regressor.predict(x_train)

##Visualizing the Training set results##
#plot the data
plt.scatter(x_train, y_train, color = "red")
#plot the regression line
plt.plot(x_train, y_pred_training, color = "blue")
plt.title("Salary vs. Experience (Training Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

##Visualizing the Test set results##
#plot the data
plt.scatter(x_test, y_test, color = "red")
#plot the regression line
plt.plot(x_train, y_pred_training, color = "blue")
plt.title("Salary vs. Experience (Test Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
