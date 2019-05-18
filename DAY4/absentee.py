# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:43:55 2019

@author: NITS
"""
with open("absentee.txt",'w') as absent:        #create the file name absentee.txt
    i=0                                     #intialize the counter
    list1 = []                                  #intialize the list
    while i<25:
        n = input("Enter the name")
        if not n:
            break
        list1.append(n)                     #insert the name in list1
        i+=1
    for item in list1:                  #enter the each input in the absentee.txt file
        absent.write(item + "\n")   
with open("absentee.txt",'rt') as abst:     #read the file
    print(abst.read())
    