# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:21:15 2019

@author: NITS
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression  



dataset = pd.read_csv("Foodtruck.csv")
features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values 
regressor = LinearRegression()  
regressor.fit(features, labels) 
val = np.array([10]).reshape(1,-1)
print("Prediction:",regressor.predict(val))



