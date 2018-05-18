#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 00:58:16 2018

@author: codyyork
"""

###Multple Linear Regression###
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv(
    "/Users/codyyork/Documents/GitHub/Machine_Learning/Regression/Multiple Linear Regression/50_Startups.csv")
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder,OneHotEncoder 
LabelEncoder_x = LabelEncoder()
x[:, 3] = LabelEncoder_x.fit_transform(x[:, 3])
 
oneHotEncoder = OneHotEncoder(categorical_features = [3])
x = oneHotEncoder.fit_transform(x).toarray()

##Avoiding the Dummy Variable Trap##
x = x[:, 1:]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

##Fitting Multiple Linear Regression to the Training set##
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

##Predicting the Test set results##
y_pred = regressor.predict(x_test)

##Building the optimal model using Backward Elimination##
import statsmodels.formula.api as sm

#only p-values
def backwardElimination(x, sl):
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
    regressor_OLS.summary()
    return x
 
SL = 0.05
x_opt = x[:, [0, 1, 2, 3, 4, 5]]
x_modeled = backwardElimination(x_opt, SL)

#p-values and r sqaured
'''
def backwardElimination(x, SL):
    numVars = len(x[0])
    temp = np.zeros((50,6)).astype(int)
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        adjR_before = regressor_OLS.rsquared_adj.astype(float)
        if maxVar > SL:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    temp[:,j] = x[:, j]
                    x = np.delete(x, j, 1)
                    tmp_regressor = sm.OLS(y, x).fit()
                    adjR_after = tmp_regressor.rsquared_adj.astype(float)
                    if (adjR_before >= adjR_after):
                        x_rollback = np.hstack((x, temp[:,[0,j]]))
                        x_rollback = np.delete(x_rollback, j, 1)
                        print (regressor_OLS.summary())
                        return x_rollback
                    else:
                        continue
    regressor_OLS.summary()
    return x
 
SL = 0.05
x_opt = x[:, [0, 1, 2, 3, 4, 5]]
x_modeled = backwardElimination(x_opt, SL)
'''











