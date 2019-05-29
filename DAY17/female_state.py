# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:51:07 2019

@author: NITS
"""

import pandas as pd
import statsmodels.api as sm


dataset = pd.read_csv("Female_stats.csv")
features = dataset.iloc[:,1:]
labels = dataset.iloc[:,0]


features = sm.add_constant(features)

features_new1 = features.iloc[:,[0,1,2]]

regressor_OLS1 = sm.OLS(endog = labels, exog = features_new1).fit()

#print(regressor_OLS1.summary())
print(regressor_OLS1.pvalues)
print(regressor_OLS1.params)




