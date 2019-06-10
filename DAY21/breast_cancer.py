# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:39:18 2019

@author: NITS
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv("breast_cancer.csv")
dataset  = dataset.iloc[:,1:]
#dataset.isnull().any(axis=0)
dataset['G'] = dataset['G'].fillna(pd.value_counts(dataset['G'],sort = True).index[0])
dataset['K_cancer'] = np.where(dataset['K']==2,0,1)

features = dataset.iloc[:,:-2]
labels = dataset.iloc[:,-1:]

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size = 0.2,random_state = 0)


from sklearn.svm import SVC
#s1 = SVC(kernel = 'rbf',random_state =0)                  #different kernal method
s1 = SVC(kernel = 'linear',random_state =0)
#s1 = SVC(kernel = 'poly',random_state =0)                 #different kernal method


s1.fit(features_train,labels_train)

labels_pred = s1.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,labels_pred)
print(cm)

print("score: ",s1.score(features_test,labels_test))

val = np.array([6,2,5,3,2,7,9,2,4]).reshape(1,-1)
diseases = s1.predict(val)
if(diseases == 1):
    print("Person have Cancer")
else:
    print("Person don't have the Cancer")