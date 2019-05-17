# -*- coding: utf-8 -*-
"""
Created on Thu May  9 23:49:43 2019

@author: NITS
"""
list1 = [1,3,6,78,35,55] 
list2 = [12,24,35,24,88,120,155]
set1 = set(list1)
set2 = set(list2)
set3 = set1.intersection(set2)
list3 = list(set3)
print(list3)