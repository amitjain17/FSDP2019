# -*- coding: utf-8 -*-
"""
Created on Sat May 18 00:03:53 2019

@author: NITS
"""
list1 = []
while True:
    info = input("Enter the name,age,roll_no: ")
    if not info:
        break
    name,age,roll_no = info.split(",")
    list1.append((name , int(age) , int(roll_no)))
list1.sort()
print("Sorted list:",list1)


    