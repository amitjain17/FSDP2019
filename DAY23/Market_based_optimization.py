+# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:06:43 2019

@author: NITS
"""

import pandas as pd
import numpy as np
from apyori import apriori
import matplotlib.pyplot as plt


dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

"""Using apply method"""
#tran = dataset.applymap(lambda x:[x] if pd.notnull(x) else []).sum(axis = 1).tolist()
#rules = list(apriori(tran, min_support = 0.003, min_confidence = 0.25, min_lift = 4))

"""Using for loop"""
dataset = dataset.replace(np.nan,"None")
list2 =[]
for i in range(0,7501):
    list1 =  []
    for j in range(0,20):
        if dataset[j][i] != "None" :
            list1.append(dataset[j][i])        
    list2.append(list1)
rules = list(apriori(list2 , min_support = 0.003, min_confidence = 0.25, min_lift = 4))
for i in range(len(rules)):
    print("Association:",rules[i][0])


list3 = []
for item in list2:
    for item1 in item:
        list3.append(item1)
filter_value = pd.DataFrame(list3)


val = filter_value[0].value_counts().head(10)
plt.bar(val.index,val)
plt.xticks(val.index,val.index,rotation=90,fontsize=10)
plt.show()
