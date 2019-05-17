# -*- coding: utf-8 -*-
"""
Created on Fri May 10 20:57:44 2019

@author: NITS
"""

name = input("Enter the file name")
with open(name , 'rt')  as line:
    lastline = line.read()
    list1 = lastline.split("\n")
    print(list1[-2])
  
    