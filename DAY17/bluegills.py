# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:08:58 2019

@author: NITS
"""

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

regressor = LinearRegression()
poly_object = PolynomialFeatures(degree = 5)


dataset = pd.read_csv("bluegills.csv")
features = dataset.iloc[:,:-1]
labels = dataset.iloc[:,-1:]

#regressor.fit(features,labels)
#plt.scatter(features,labels)
#plt.plot(features, regressor.predict(features))

features_poly = poly_object.fit_transform(features)

regressor2 = LinearRegression()
regressor2.fit(features_poly, labels)
#regressor2.fit(features_poly, labels)

val = np.array([5]).reshape(1,-1)
print(regressor2.predict(poly_object.transform(val)))



