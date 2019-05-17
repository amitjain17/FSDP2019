# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:03:53 2019

@author: NITS
"""

def leap(a):
    if a%4==0:
       print ("year is leap year")
       return True
    else:
       print("year is not leap year")
       return False

x = int(input("Enter the year"))
leap(x)

