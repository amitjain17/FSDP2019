# -*- coding: utf-8 -*-
"""
Created on Fri May 10 20:09:58 2019

@author: NITS
"""
dict1 ={}


with open("romeo.txt",'rt') as rom:             #open the file using file handling
         line1 = rom.readlines()            #read each line in the file
         
         for item in line1:                 #split each letter for count
            list1 = item.split()
            
            for raw in list1:               #read each letter and count in the dictionary
                if raw in dict1.keys():
                    dict1[raw] = dict1[raw] + 1
                else:
                    count = 1
                    dict1[raw] = count

print(dict1)
   
