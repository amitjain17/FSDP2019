# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:51:25 2019

@author: NITS
"""

import pandas as pd

dataset = pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",delimiter = ' ')

lpsa_mean = dataset['lpsa'].mean()
dataset["lpsa"] = dataset["lpsa"].apply(lambda x: 1 if x>lpsa_mean else 0)

features = dataset.iloc[:,:-1]
labels  =dataset.iloc[:,-1:]

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size = 0.3,random_state=0)

from sklearn.linear_model import LogisticRegression
classification = LogisticRegression()
classification.fit(features_train,labels_train)

labels_pred = classification.predict(features_test)
score1 = classification.score(features_train,labels_train)
score2 = classification.score(features_test,labels_test)
print("Train_logistic:",score1)
print("Test_logistic:",score2)

from sklearn.neighbors import KNeighborsClassifier
cl = KNeighborsClassifier(n_neighbors=5,p=2)
cl.fit(features_train,labels_train)

print("Train_kNN:",cl.score(features_train,labels_train))
print("Test_kNN:", cl.score(features_test,labels_test))


from sklearn.tree import DecisionTreeClassifier
d1 = DecisionTreeClassifier()
d1.fit(features_train,labels_train)

print("Train_decision:",d1.score(features_train,labels_train))
print("Test_Decision:",d1.score(features_test,labels_test))

from sklearn.ensemble import RandomForestClassifier
r1 = RandomForestClassifier(n_estimators=20,random_state=0)
r1.fit(features_train,labels_train)

print("Train_forest:",r1.score(features_train,labels_train))
print("Test_Forest:",r1.score(features_test,labels_test))