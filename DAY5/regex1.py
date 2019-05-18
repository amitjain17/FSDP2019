# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:13:12 2019

@author: NITS
"""
                            
import re                               #import regular expression
while True: 
    list1 = []                      #insert the value
    value  = input("Enter the value")   
    if not value:
        break
    else:
        list1.append(value)             #insert all value in list1
    for item in list1:
#        for item in re.match(r'?/d/./d',string):
        if re.match(r'^[+-]?\d*\.\d+$',item):       #use regex format for checking that number is float or not
            print("True")
        else:
            print("False")








