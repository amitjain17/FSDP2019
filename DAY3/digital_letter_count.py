# -*- coding: utf-8 -*-
"""
Created on Thu May  9 23:04:30 2019

@author: NITS
"""
dict1 = {}
list4 =[]
m=0
p=1
while True:
    n = input("Enter the string")
    if not n:
        break
    #i = 0
   # i+=1
    list1 = n.split()
    list2 = "".join(list1[:-1])
    list3= list1[-1]
    dict1[list2] = m
    m+=2
    dict1[list3]= p
    p+=2
for i in dict1.values():
    if i%2 == 0:
        for j in dict1.keys():    
            list4 = len(j)
            print("letters : ",list4)
    #break
    elif (i%2 !=0):
        for j in dict1.keys():    
            list4 = len(j)
            print("Numbers : ",list4)
    break
        
    
    
    
         
    