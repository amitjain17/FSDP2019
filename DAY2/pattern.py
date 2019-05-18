# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:42:53 2019

@author: NITS
"""

n = int(input("Enter the number"))      #take input from user
for i in range(n):                      #run loop for rows
    print("\n")
    for j in range(i+1):                  #run loop for coloumn
      print('* ',end="")                 #print * 
for n in range(n,1,-1):                 #run loop for rows in reverse
    print("\n")
    for m in range(n-1):                  #run loop for coloumn in reverse
        print('* ',end="")