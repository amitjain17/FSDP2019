# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:58:32 2019

@author: NITS
"""

import pandas as pd 

from sklearn import datasets
da = datasets.load_iris()

features = da.data
features_name = da.feature_names
labels = da.target
labels_name = da.target_names.reshape(1,-1)

features_df	= pd.DataFrame(features, columns= features_name)

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features_df,labels,test_size = 0.2,random_state = 0)


from sklearn.svm import SVC
#s1 = SVC(kernel = 'rbf',random_state=0)
#s1 = SVC(kernel = 'linear',random_state=0)
s1 = SVC(kernel = 'poly',random_state=0)

s1.fit(features_train,labels_train)
labels_pred = s1.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_pred,labels_test)
print(cm)

print("Score:",s1.score(features_test,labels_test))

