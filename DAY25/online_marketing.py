# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 22:55:06 2019

@author: NITS
"""

import pandas as pd
import sqlite3


da = sqlite3.connect("online_marketing.db")
a = da.cursor()

#a.execute("SELECT * FROM emp")
 
ans = a.fetchall()
for i in ans:
    print(i)