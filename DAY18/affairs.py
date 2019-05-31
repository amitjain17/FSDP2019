# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:36:23 2019

@author: NITS
"""

import pandas as pd
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
dataset = pd.read_csv("affairs.csv")
features = dataset.iloc[:,:-1]
labels = dataset.iloc[:,-1:]

from sklearn.preprocessing import OneHotEncoder
value = OneHotEncoder(categorical_features = [6])
features = value.fit_transform(features).toarray()
features = features[:,1:]

value = OneHotEncoder(categorical_features = [11])
features = value.fit_transform(features).toarray()
features = features[:,1:]

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
features_train = scaler.fit_transform(features_train)
features_test = scaler.transform(features_test)


from sklearn.linear_model import LogisticRegression
classification = LogisticRegression()
classification.fit(features_train,labels_train)

labels_pred = classification.predict(features_test)

score1 = classification.score(features_train,labels_train)
score2 = classification.score(features_test,labels_test)
print(score1)
print(score2)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_pred,labels_test)