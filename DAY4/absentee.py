# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:43:55 2019

@author: NITS
"""
with open("absentee.txt",'w') as absent:
    i=0
    list1 = []
    while i<25:
        n = input("Enter the name")
        if not n:
            break
        list1.append(n)
        i+=1
    for item in list1:
        absent.write(item + "\n")
with open("absentee.txt",'rt') as abst:
    print(abst.read())
    