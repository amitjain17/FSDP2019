# -*- coding: utf-8 -*-
"""
Created on Fri May 10 00:02:34 2019

@author: NITS
"""

list1 =[1,3,6,78,35,55,1]       #enter the first list
list2 = []                      #intialize the second list
for i in list1:             #for each element in list1
    if i not in list2:          #if the item is not in list2 insert the item in list
        list2.append(i)
        
   
print (list(list2))
    