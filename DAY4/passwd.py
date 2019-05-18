# -*- coding: utf-8 -*-
"""
Created on Fri May 10 21:30:55 2019

@author: NITS
"""
dict1 = {}                          #Initialize the dictionary
with open("passwd",'r') as ps:      #open the file
#    
#    a = ps.read()
#    list1 = a.split("_")
    for item in ps:                        #split each element which is seperated from ':'
        list2 = item.split(":")
        
#        print(list2) 
        dict1[list2[0]] = list2[2]         #insert the information in the dictionary
       
print(dict1)
   
    