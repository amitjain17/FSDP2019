# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:03:53 2019

@author: NITS
"""

def leap(yr):                   #create function
    if yr%4 == 0 and yr%100 !=0 or yr%400 ==0:   #if the number is divided by 4 and 400 than the number is leap year
           print ("year is leap year")
           return True
    else:            #number is not leap year
       print("year is not leap year")
       return False

year = int(input("Enter the year"))     #enter the number for checking the leap year or not
leap(year)

