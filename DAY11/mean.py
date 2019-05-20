# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:10:25 2019

@author: NITS
"""

import numpy as np

list1 = [13, 18, 13, 14, 13, 16, 14, 21, 13]             #insert the value in list
arr= np.array(list1)                              #convert the list in array
print("Mean : ",np.mean(arr))                      #find the mean of array and print it
print("Medium:",np.median(arr))                    #find the median of array and print it
Range = np.max(list1)-np.min(list1)
print("Range:",Range)                           #find the range and print it
