# -*- coding: utf-8 -*-
"""
Created on Fri May 10 21:30:55 2019

@author: NITS
"""
dict1 = {}
with open("passwd",'r') as ps:
#    
#    a = ps.read()
#    list1 = a.split("_")
    for item in ps:
        list2 = item.split(":")
        
#        print(list2) 
        dict1[list2[0]] = list2[2]
       
print(dict1)
   
    