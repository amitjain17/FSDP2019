# -*- coding: utf-8 -*-
"""
Created on Fri May 10 00:02:34 2019

@author: NITS
"""

list1 =[1,3,6,78,35,55,1] 
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
        
   
print (list(list2))
    