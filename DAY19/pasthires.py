# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:44:48 2019

@author: NITS
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv("PastHires.csv")

dataset =dataset.replace("Y",1)
dataset =dataset.replace("N",0)
    
features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,-1:].values

from sklearn.preprocessing import LabelEncoder
l1 = LabelEncoder()
features[:,3] = l1.fit_transform(features[:,3])


from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.20,random_state=0)

from sklearn.tree import DecisionTreeRegressor
tree = DecisionTreeRegressor()
tree.fit(features_train,labels_train)
labels_pred=tree.predict(features_test)
print("Test:",tree.score(features_test,labels_test))
print("Train:",tree.score(features_train,labels_train))
from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  


from sklearn.ensemble import RandomForestClassifier
regressor1 = RandomForestClassifier(n_estimators=10, random_state=0)  
regressor1.fit(features_train, labels_train) 

val1 = np.array([10,1,4,0,1,0]).reshape(1,-1)
print("Predicton 1:",regressor1.predict(val1))


val2 = np.array([10,0,4,1,0,1]).reshape(1,-1)
print("Prediction 2:",regressor1.predict(val2))


