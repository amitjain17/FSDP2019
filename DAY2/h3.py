# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:14:39 2019

@author: NITS
"""
list1=["january","march","may","july","august","october","december"]
list2=["april","june","september","november"]
list3=["february"]
def days_in_month(month):    #define the function if the month have present in list1 than print 31
                            #and if the month have present in list2 than print 30
                            #and if the month have present in list3 than check if the year is leap year than print 29 else print 28
                            
    mon = month.lower()
    for i in list1: 
       if i == mon:
        print("Month: 31")
        break
    for y in list2:
       if y == mon:
        print("Month: 30")
        break
    for z in list3:
        if z == mon:
            year = int(input("Enter the year"))
            if year%4 == 0 and year%100 !=0 or year%400 == 0 :
                print("Month days: 29")
            else:
                print("Month days: 28")
            break
            

month= str(input("Enter the month"))
days_in_month(month)            #call the function to check the number of days in month      