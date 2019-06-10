# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:20:59 2019

@author: NITS
"""

import pandas as pd

dataset  = pd.read_csv("monster_com-job_sample.csv")
dataset['organization'] = dataset['organization'].fillna("missing")

dataset.isnull().any(axis=0)

dataset['organization'].apply(lambda x:  dataset['organization'],dataset['location']= dataset['location'], dataset['organization']  if x[-4]=="," else dataset['organization'])


