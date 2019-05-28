# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:08:32 2019

@author: NITS
"""


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("Bahubali2_vs_Dangal.csv")

features = dataset.iloc[:, :-2].values
labels = dataset.iloc[:, -2:].values
frames_train,frames_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)

regressor = LinearRegression()  
regressor.fit(frames_train, labels_train) 
val = np.array([10]).reshape(1,-1)
print("Prediction:",regressor.predict(val))

