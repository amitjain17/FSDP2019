# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 11:09:57 2019

@author: NITS
"""

import pandas as pd 
#import numpy as np
import matplotlib.pyplot as plt


train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
dataset = train.append(test)
features = dataset.iloc[:,:562].values
labels = dataset.iloc[:,-1:].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.3,random_state=0)


from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(features_train,labels_train)

labels_pred = classifier.predict(features_test)

#print("Train_score_DTC:",classifier.score(features_train,labels_train))
#print("Test_score_DTC:",classifier.score(features_test,labels_test))
#
from sklearn.metrics import confusion_matrix,accuracy_score
#cm = confusion_matrix(labels_test,labels_pred)
#print(cm)

#Using RandomForestClassifier train the model and find the score

from sklearn.ensemble import RandomForestClassifier
cl = RandomForestClassifier(n_estimators = 10 , random_state=0)
cl.fit(features_train,labels_train)

labels_cl_pred = cl.predict(features_test)

print("Train_score_RFC:",cl.score(features_train,labels_train))
print("Test_score_RFC:",cl.score(features_test,labels_test))

#cm_RFC = confusion_matrix(labels_test,labels_cl_pred)
#print(cm_RFC)

#Using LogisticRegression train the model and find the score

from sklearn.linear_model import LogisticRegression 
lr = LogisticRegression()
lr.fit(features_train,labels_train)

labels_pred_LR = lr.predict(features_test)
print("Train_score_LR:",lr.score(features_train,labels_train))
print("Test_score_LR:",lr.score(features_test,labels_test))

#cm_LR = confusion_matrix(labels_test,labels_pred_LR)
#print(cm_LR)

#Using kNN train the model and find the score

from sklearn.neighbors import KNeighborsClassifier
knc  = KNeighborsClassifier(n_neighbors=5,p=2)
knc.fit(features_train,labels_train)

labels_pred_KNC = knc.predict(features_test)
print("Train_score_KNN:",knc.score(features_train,labels_train))
print("Test_score_KNN:",knc.score(features_test,labels_test))

#cm_KNN = confusion_matrix(labels_test,labels_pred_KNC)
#print(cm_KNN)

p1 = accuracy_score(labels_test,labels_pred_LR)
p2 = accuracy_score(labels_test,labels_cl_pred)
p3 = accuracy_score(labels_test,labels_pred)
p4  =accuracy_score(labels_test,labels_pred_KNC)
print("accuracy_score_LR:",accuracy_score(labels_test,labels_pred_LR))
print("accuracy_score_RFC:",accuracy_score(labels_test,labels_cl_pred))
print("accuracy_score_DTC:",accuracy_score(labels_test,labels_pred))
print("accuracy_score_KNC:",accuracy_score(labels_test,labels_pred_KNC))
plt.bar(["Logistic","RandomForest","DecisionTree","KNN"],[p1,p2,p3,p4])
plt.show()

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
labels=lb.fit_transform(labels)

import statsmodels.api as sm
features = sm.add_constant(features)

list1 = []
p = []
features_opt = features[:,:]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
p = list(regressor_OLS.pvalues)

n=0
for i in p:
    if i>0.5:
        n +=1
    else:
        list1.append(n)
        n +=1

fe = features[:,list1]

"""train test split"""
features_train,features_test,labels_train,labels_test = train_test_split(fe,labels,test_size=0.3,random_state=0)

"""Decision Tree Classifier"""
cl1 = DecisionTreeClassifier()
cl1.fit(features_train,labels_train)

labels_pred1 = cl1.predict(features_test)
print("accuracy_score_DTC:",accuracy_score(labels_test,labels_pred1))

"""Random Forest"""
cl2 = RandomForestClassifier(n_estimators = 10 , random_state=0)
cl2.fit(features_train,labels_train)

labels_cl2_pred = cl2.predict(features_test)
print("accuracy_score_RFC:",accuracy_score(labels_test,labels_cl2_pred))


"""Logistic Regressoion"""
lr1 = LogisticRegression()
lr1.fit(features_train,labels_train)

labels_pred_LR1 = lr1.predict(features_test)
print("accuracy_score_LR:",accuracy_score(labels_test,labels_pred_LR1))


"""KNN"""
knc1  = KNeighborsClassifier(n_neighbors=5,p=2)
knc1.fit(features_train,labels_train)

labels_pred_KNC1 = knc1.predict(features_test)
print("accuracy_score_KNC:",accuracy_score(labels_test,labels_pred_KNC1))

p5 = accuracy_score(labels_test,labels_pred_LR1)
p6 = accuracy_score(labels_test,labels_cl2_pred)
p7 = accuracy_score(labels_test,labels_pred1)
p8  =accuracy_score(labels_test,labels_pred_KNC1)

plt.bar(["Logistic","RandomForest","DecisionTree","KNN"],[p5,p6,p7,p8])
plt.show()
