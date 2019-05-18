# -*- coding: utf-8 -*-
"""
Created on Sat May 18 19:17:42 2019

@author: NITS
"""
from functools import reduce   #import reduce function from fuctools
list1 = []                      #intialize the list1

while True:                     #take input from user
    n = input("Enter the values")
    if not n:
        break
    list1.append(n)                 #insert the value in list1

odd1  = reduce(lambda y,z: y*z ,filter(lambda x: x % 2==1,list1))  #find the product of odd number in list1

print("odd number product:",odd1)               #print the odd product value
