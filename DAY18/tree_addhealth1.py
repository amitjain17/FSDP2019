# -*- coding: utf-8 -*-
"""
Created on Wed May 29 21:03:34 2019

@author: NITS
"""

import pandas as pd

dataset = pd.read_csv("tree_addhealth.csv")
features = dataset.iloc[:,[0,1,2,3,4,5,6,8,9,10,11,12,13,14,15]]
labels = dataset.iloc[:,7:8]

#features.isnull().any(axis=0)
features['age'] = features['age'].fillna(features['age'].median())
features['ESTEEM1'] = features['ESTEEM1'].fillna(features['ESTEEM1'].median())

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size = 0.2,random_state = 0)


from sklearn.linear_model import LogisticRegression
value = LogisticRegression()
value.fit(features_train,labels_train)

labels_pred = value.predict(features_test)

score1 = value.score(features_train,labels_train)
score2 = value.score(features_test,labels_test)
print(score1)
print(score2)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,labels_pred)
print(cm)
