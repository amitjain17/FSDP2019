# -*- coding: utf-8 -*-
"""
Created on Thu May  9 00:11:10 2019

@author: NITS
"""
temp=0

def add(list2):
    c=0
    for i in list2:
        c+=i
    return c
def mul(list2):
    c=1
    for i in list2:
        c= c*i
    return c
def large(list2):
    list2.sort()
    c = list2[-1]
    return c
def small(list2):
    list2.sort()
    c = list2[0]
    return c
def sort(list2):
    list2.sort()
    c = list2
    return c
def Remove_Duplicate(list2):
     a = set(list2)
     return a

list1 = []

for i in range(5):
    n = int(input("Enter the values in list"))      #enter the values
    list1.append(n)
    
print(list1)
print("Addition:",add(list1))                   #call the function addition
print("Multiplication:",mul(list1))                 #call the function of multiplication
print("Largest number:",large(list1))               #call the function of largest number
print("Smallest number:",small(list1))          #call the function of smallest number
print("sorted list:",sort(list1))               #call the function of sorting the list
print("Remove duplicate",list(Remove_Duplicate(list1)))     #call the function to duplicate number