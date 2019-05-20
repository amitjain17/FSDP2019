# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:09:24 2019

@author: NITS
"""

import numpy as np
from collections import Counter



arr = np.random.randint(1,15,40)        #create random number from 1 to 15

list1 = list(arr)              #convert the array in list
c = Counter(list1)             #counter the value for counting how much time it will be come
dict1 = dict(c)                #convert the counter tuple in dictionary
print(dict1)                   
z = max(dict1.values())        #find the maximum value in dictionary
for key,value in dict1.items():       #find the key correspond to max value
    if z == value:
        print("Key value:",key)
        
    
"""Using numpy"""  
    
#count = np.bincount(list1)
#max_value = np.argmax(count)
#print("Max_value: ",max_value)

    