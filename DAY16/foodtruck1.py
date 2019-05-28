# -*- coding: utf-8 -*-
"""
Created on Mon May 27 22:23:10 2019

@author: NITS
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("Foodtruck.csv")
frames  = dataset.iloc[:,:-1]
labels  = dataset.iloc[:,1]
frames_train,frames_test,labels_train,labels_test = train_test_split(frames,labels,test_size=0.2,random_state = 0)
regression = LinearRegression()
regression.fit(frames_train,labels_train)

#pre = regression.predict(frames_test)
#df = pd.DataFrame(pre,labels_test)
x = np.array([3.073]).reshape(1,-1)
pred= regression.predict(x)
 