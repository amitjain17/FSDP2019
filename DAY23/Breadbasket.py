# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:38:01 2019

@author: NITS
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from apyori import apriori

dataset = pd.read_csv("BreadBasket_DMS.csv")
dataset['Item'] = dataset['Item'].replace('NONE',np.nan)
dataset = dataset.dropna()
d = dataset['Item'].value_counts()

top_value = d.head(15)
plt.pie(top_value,labels = top_value.index,autopct='%1.2f',startangle=90,radius=2)
plt.show()

val = dataset.groupby('Transaction')['Item']
tran = list(val.apply(lambda x : list(set(x))))


rules = list(apriori(tran, min_support = 0.0025, min_confidence = 0.2, min_lift = 3))
for i in range(len(rules)):
    print("Association:",rules[i].items)
    print("item_base",rules[i].ordered_statistics[0][0])
    print("item_add",rules[i].ordered_statistics[0][1])
    print("confidence",rules[i].ordered_statistics[0][2])
    print("lift",rules[i].ordered_statistics[0][3],"\n")


