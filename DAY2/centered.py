# -*- coding: utf-8 -*-
"""
Created on Sat May 18 00:20:45 2019

@author: NITS
"""
list1 = []
list2 = []
while True:
    n  = input("Enter the values")
    if not n:
        break
    list1.append(n)
    list2.append(n)
list1.sort()
Largest = list1[len(list1)]
Smallest = list1[0]
