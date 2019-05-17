# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:42:52 2019

@author: NITS
"""
list1 = []                                  # create the new list
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida'] #write the list of inputs
vowels = ['a','e','i','o','u']                           #create vowels
for i in state_name:                            # run loop in state name
    list2 = []                              # create new list
    for j in i.lower():                     # run loop in particular string
        if j not in vowels:                 # check in particular string  and add in list
            list2.append(j)                 
    list1.append(''.join(list2))
print(list1)
            
        