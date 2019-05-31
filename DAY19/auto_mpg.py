# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:30:34 2019

@author: NITS
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv("Auto_mpg.txt",delimiter = "\s+",header = None)
#dataset1 = pd.read_csv("Auto_mpg.txt",delim_whitespace=True)
dataset.columns = ["mpg", "cylinders", "displacement","horsepower","weight","acceleration",
     "model year", "origin", "car name"]

dataset["horsepower"] = dataset["horsepower"].replace("?",np.nan).astype('float64')
x = dataset["horsepower"].mean()
dataset["horsepower"] = dataset["horsepower"].fillna(x)


features = dataset.iloc[:,1:]
features = features.drop('car name',axis = 1)
labels = dataset['mpg']

data = dataset['car name'][dataset['mpg'] == dataset['mpg'].max()]
print(data)


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20,random_state=0)  

from sklearn.tree import DecisionTreeRegressor  
classifier = DecisionTreeRegressor()  
classifier.fit(features_train, labels_train)

val =np.array([6,215,100,2630,22.2,80,3]).reshape(1,-1)
print("decision_tree:",classifier.predict(val))

from sklearn.ensemble import RandomForestRegressor
regressor1 = RandomForestRegressor(n_estimators=20, random_state=0)  
regressor1.fit(features_train, labels_train) 

print("Random_forest:",regressor1.predict(val)) 


