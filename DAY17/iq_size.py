# -*- coding: utf-8 -*-
"""
Created on Tue May 28 18:20:32 2019

@author: NITS
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

regressor = LinearRegression()
dataset = pd.read_csv("iq_size.csv")
features = dataset.iloc[:,1:].values
labels = dataset.iloc[:,:-3].values

features = sm.add_constant(features)

features_opt = features[:, [0, 1, 2, 3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
print(regressor_OLS.summary())

features_opt = features[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
print(regressor_OLS.summary())

features_opt = features[:, [ 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
print(regressor_OLS.summary())

features_opt = features[:, [1]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
print(regressor_OLS.summary())


regressor.fit(features_opt,labels)
val = np.array([90]).reshape(1,-1)
print(regressor.predict(val))