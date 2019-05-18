# -*- coding: utf-8 -*-
"""
Created on Thu May  9 21:58:16 2019

@author: NITS
"""

dict1 = {}                              #intialize the dictionary
def teen(x):
    if x == 13 or x== 14 or x == 17 or x == 18 or x == 19:     #if the value is 13 ,14 ,17,18,19 then final value is zero
        return 0
    else:
        return x
    
def sum(dict2):                             #Sum all the value which is present in dictionary
    c = 0
    for i in list(dict2.values()):
       m = teen(i)
       c = c+m
    return c
        

while True:
    n = input("Enter the number and string")             #enter the number and string from user
    if not n:
        break
    list1 = n.split()
    list2 = "".join(list1[:-1])
    list3 = int(list1[-1])
    dict1[list2]=list3
print(sum(dict1))
print(dict1)