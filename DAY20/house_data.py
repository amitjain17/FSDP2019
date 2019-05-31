# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:22:32 2019

@author: NITS
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv("kc_house_data.csv")
dataset['date'] = dataset['date'].apply(lambda x: x[:4]).astype(int)
#dataset.isnull().any(axis=0)
dataset["sqft_above"] = dataset["sqft_above"].fillna(dataset["sqft_above"].mean())

features = dataset.drop(["id","price"],axis=1)
labels = dataset['price']

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state = 0)

from sklearn.linear_model import LinearRegression
l1 = LinearRegression()
l1.fit(features_train,labels_train)

labels_pred = l1.predict(features_test)

from sklearn import metrics
print("Mean_squared_error_linear:",metrics.mean_squared_error(labels_test,labels_pred))
print ("labels_mean",np.mean(dataset.values[:,2]))

print("score_train",l1.score(features_train,labels_train))
print("score_test",l1.score(features_test,labels_test))

print("")
from sklearn.linear_model import Lasso
la1 = Lasso()
la1.fit(features_train,labels_train)
labels_pred_lasso = la1.predict(features_test)

print("Mean_squared_error_lasso:",round(metrics.mean_squared_error(labels_test,labels_pred_lasso),3))
print("score_train_lasso: ",la1.score(features_train,labels_train))
print("score_test_lasso: ",la1.score(features_test,labels_test))

print("")
from sklearn.linear_model import Ridge
r1 = Ridge()
r1.fit(features_train,labels_train)
labels_pred_ridge = r1.predict(features_test)

print("Mean_squared_error_ridge:",round(metrics.mean_squared_error(labels_test,labels_pred_ridge),3))
print("score_train_ridge: ",r1.score(features_train,labels_train))
print("score_test_ridge: ",r1.score(features_test,labels_test))
