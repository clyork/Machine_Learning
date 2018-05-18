#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 23:47:14 2018

@author: codyyork
"""

###Polynomial Regression###

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv("/Users/codyyork/Documents/GitHub/Machine_Learning/Regression/Polynomial Regression/Position_Salaries.csv")

#should do 1:2 to get rid of any warnings
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

#there are too few pieces of data to split it up and we want to be as accurate as possible

##Fitting Polynomial Regression to the Dataset##
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
poly_regressor = PolynomialFeatures(degree = 4)
x_poly = poly_regressor.fit_transform(x)
linear_regressor = LinearRegression()
linear_regressor.fit(x_poly, y)

##Visualizing the Polynomial Regression Results##
x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(x, y, color='red')
plt.plot(x_grid, linear_regressor.predict(poly_regressor.fit_transform(x_grid)), color = 'blue')
plt.title("Truth or Bluff (Polynomial Regression)")
plt.xlabel("Position")
plt.ylabel("Salary")
plt.show()

##Predicting a new result with Polynomial Regression##
linear_regressor.predict(poly_regressor.fit_transform(6.5))







