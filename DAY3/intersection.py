# -*- coding: utf-8 -*-
"""
Created on Thu May  9 23:49:43 2019

@author: NITS
"""
list1 = [1,3,6,78,35,55]                    #Enter the first list
list2 = [12,24,35,24,88,120,155]            #enter the secnond list
              
set3 = set(list1).intersection(set(list2))   #find the intersection in between two list
list3 = list(set3)
print(list3)