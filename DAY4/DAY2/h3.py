# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:14:39 2019

@author: NITS
"""
list1=["januaray","feburary","march","april"]
def days_in_month(a):
    print("month=")
    if a== "januaray":
        print("31")
    if a == "febuaray":
        print("28")
    if a== "march":
        print("30")
    if a== "april":
        print("31")

x= str(input("Enter the month"))
days_in_month(x)        