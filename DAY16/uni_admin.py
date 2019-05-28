# -*- coding: utf-8 -*-
"""
Created on Mon May 27 22:58:24 2019

@author: NITS
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv("University_data.csv")
features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,-1].values

regressor = LabelEncoder()
features[:, 0] = regressor.fit_transform(features[:, 0])
onehotencoder = OneHotEncoder(categorical_features=[0])
features = onehotencoder.fit_transform(features).toarray()
features = features[:,1:]

features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)
regressor1 = LinearRegression()
regressor1.fit(features_train,labels_train)
pre = regressor1.predict(features_test)
dataframe = pd.DataFrame({"Predicted":pre,"Given":labels_test})
print(dataframe)



