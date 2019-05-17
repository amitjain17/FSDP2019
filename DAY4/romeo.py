# -*- coding: utf-8 -*-
"""
Created on Fri May 10 20:09:58 2019

@author: NITS
"""
dict1 ={}


with open("romeo.txt",'rt') as rom:
         line1 = rom.read()
         list2 = line1.split("\n")
         for item in list2:
            list1 = item.split()
            
            for raw in list1:
                if raw in dict1.keys():
                    dict1[raw] = dict1[raw] + 1
                else:
                    count = 1
                    dict1[raw] = count

print(dict1)
   
