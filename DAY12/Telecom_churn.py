# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:48:11 2019

@author: NITS
"""

import pandas as pd

df = pd.read_csv("Telecom_churn.csv")
df1 = df['voice mail plan'][df['international plan']== 'yes'].value_counts()
print("Person_with_voice_main and international_plan: ",df1[1])
churn_true = df['total intl charge'][df['churn']==True].sum()
churn_false = df['total intl charge'][df['churn']==False].sum()
print(" Churn_true :",churn_true,"\n","Churn_false :",churn_false)

new = df['total night calls'][df['churn']==True].max()
state = df['state'][df['total night calls']==new]
print("State :",state)

