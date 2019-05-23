# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:12:30 2019

@author: NITS
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Automobile.csv")
df1 = df['make'].value_counts()
max_value = (0.1,0,0,0,0,0,0,0,0,0,0)

plt.pie(df1.values[0:11], explode = max_value, labels=df1.index[0:11],autopct='%1.2f%%')

