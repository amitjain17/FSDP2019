# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:51:04 2019

@author: NITS
"""



list1 = []  #intialize the list

for i in range(1,21):           #Run the loop from 1 to 20
    list1.append(i)                 #insert the value in list1
print("Odd numbers:",list1[0::2])              #print the odd value
print("Even numbers:",list1[1::2])              #print the even value