# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:00:17 2019

@author: NITS
"""
list1 = []
while True:    
    input1 = input("Enter the value")
    if not input1:
        break
    list1.append(input1)
#for item in list1:
#    num =item
#    new =num [::-1]
#    if new == num:
#        list
#    else:
#        print("Not pallindrome")
num = all([int(i)>0 for i in list1]) and any([i==i[::-1] for i in list1])
    
