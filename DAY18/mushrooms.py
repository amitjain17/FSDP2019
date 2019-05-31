# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:18:57 2019

@author: NITS
"""

import pandas as pd

dataset = pd.read_csv("mushrooms.csv")
features = dataset.iloc[:,[5,-1,-2]].values
labels = dataset.iloc[:,:1].values

from sklearn.preprocessing import LabelEncoder
l1 = LabelEncoder()
features[:, 0] = l1.fit_transform(features[:, 0])
l2 = LabelEncoder()
features[:, 1] = l2.fit_transform(features[:, 1])
l3 = LabelEncoder()
features[:, 2] = l3.fit_transform(features[:, 2])

l4 = LabelEncoder()
labels = l4.fit_transform(labels)



from sklearn.preprocessing import OneHotEncoder
o1 = OneHotEncoder(categorical_features=[0])
features = o1.fit_transform(features).toarray()
features = features[:,1:]

o2 = OneHotEncoder(categorical_features=[-2])
features = o2.fit_transform(features).toarray()
features = features[:,1:]

o3 = OneHotEncoder(categorical_features=[-1])
features = o3.fit_transform(features).toarray()
features = features[:,1:]


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LogisticRegression
classification = LogisticRegression()
classification.fit(features_train,labels_train)

labels_pred = classification.predict(features_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_pred,labels_test)
print(cm)
