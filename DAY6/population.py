# -*- coding: utf-8 -*-
"""
Created on Wed May 15 00:52:57 2019

@author: NITS
"""
from collections import Counter

dict1 = {}
list1 =[]
list2= []
import csv
with open("population.csv") as popu:
   # new = csv.reader(popu,delimiter = ",")
    new1 = csv.DictReader(popu)
    for item in new1:
        list1.append(dict(item))
       # print(dict(item))
    for new in list1:
        
         