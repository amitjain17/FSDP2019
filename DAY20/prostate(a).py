# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:46:35 2019

@author: NITS
"""
import pandas as pd
import numpy as np

dataset = pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",delimiter = ' ')
features = dataset.iloc[:,:-1]
labels  =dataset.iloc[:,-1:]

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size = 0.3,random_state=0)

from sklearn.linear_model import LinearRegression
l1 = LinearRegression()
l1.fit(features_train,labels_train)

labels_pred = l1.predict(features_test)
#df = pd.DataFrame(labels_pred,labels_test)
print("score_train",l1.score(features_train,labels_train))
print("score_test",l1.score(features_test,labels_test))


from sklearn import metrics
print("Mean_squared_error_linear:",metrics.mean_squared_error(labels_test,labels_pred))

print ("labels_mean",np.mean(dataset.values[:,-1]))


from sklearn.linear_model import Ridge
r1 = Ridge()
r1.fit(features_train,labels_train)
labels_pred_ridge = r1.predict(features_test)

print("Mean_squared_error_ridge:",round(metrics.mean_squared_error(labels_test,labels_pred_ridge),3))

from sklearn.linear_model import Lasso
la1 = Lasso()
la1.fit(features_train,labels_train)
labels_pred_lasso = la1.predict(features_test)

print("Mean_squared_error_lasso:",round(metrics.mean_squared_error(labels_test,labels_pred_lasso),3))







