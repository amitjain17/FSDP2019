# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:34:38 2019

@author: NITS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("data.csv")
da = dataset['Country'].value_counts()


plt.pie(da,labels=da.index,autopct='%1.2f%%')

plt.legend(da.index,loc="centre left",bbox_to_anchor=(1,0,0.5,1))
plt.axis('equal')
plt.show()



list1 =[0.1,0.2]
for i in range(16):
    list1.append(0.0)
explode = tuple(list1)
cl = dataset['Classification'].value_counts()
plt.pie(cl,labels=cl.index,autopct='%1.2f%%',explode=explode)
plt.title("Top 2 Classification")
plt.show()



list2 =[0.1,0.2]
for i in range(49):
    list2.append(0.0)
explode = tuple(list2)
dl = dataset['Culture'].value_counts()
plt.pie(dl,labels=dl.index,autopct='%1.2f%%',explode=explode)
plt.title("Top 2 Culture")
plt.show()
