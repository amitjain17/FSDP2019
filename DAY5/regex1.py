# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:13:12 2019

@author: NITS
"""

import re
while True: 
    list1 = []
    value  = input("Enter the value")
    if not value:
        break
    else:
        list1.append(value)
    for item in list1:
#        for item in re.match(r'?/d/./d',string):
        if re.match(r'^[+-]?\d*\.\d+$',item):
            print("True")
        else:
            print("False")








