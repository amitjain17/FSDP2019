# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:34:24 2019

@author: NITS
"""
""" String Handling"""

string = str(input("Enter the First name and last name with spacing"))
n = str.split(string)                          #split the string

print(n[1]+" "+n[0])                         # print the split string in reverse order

