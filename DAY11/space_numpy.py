# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:50:40 2019

@author: NITS
"""
import numpy as np
list1 = []                             #intialize list
n =0                                   #intialize counter
while n<9:
    value = input("Enter the Value:")
    
    list1.append(int(value))        #append the value in list
    n+=1                             #increase the counter
arr = np.array(list1)                #convert the list in array
arr = arr.reshape(3,3)              #reshape the array in 3*3 matrix
print(np.array(arr))