# -*- coding: utf-8 -*-
"""
Created on Fri May 10 20:57:44 2019

@author: NITS
"""

name = input("Enter the file name")                 #take the file name from user
with open(name , 'rt')  as line:                    #open the file
    lastline = line.read()                          #read full file
    list1 = lastline.split("\n")                #store each value in list1
    print(list1[-2])                            #print last line
  
    