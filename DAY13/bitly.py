# -*- coding: utf-8 -*-
"""
Created on Wed May 22 20:55:12 2019

@author: NITS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_json("usagov_bitly_data.json",lines=True)
df = df.replace(np.nan,"Mising")
df = df.replace("","Unknown")
new = df['tz'].value_counts().head(10)

#####################################################

"""with out using dataframe"""

list1 = Counter(df['tz']).most_common()
top_ten = list1[:10]

####################################################

index = [0,1,2,3,4,5,6,7,8,9]

plt.bar(index,new)
plt.xticks(index,new.index,rotation=90,fontsize=10)


browser = df['a'].value_counts().head(5)
plt.bar([0,1,2,3,4],browser,align='center',alpha=1.0)
#plt.xticks([0,1,2,3,4],browser.index,rotation=90)