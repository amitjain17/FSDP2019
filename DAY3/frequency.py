# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:39:11 2019

@author: NITS
"""

dict1 = {}                  #intialize the dictionary
list1 =[]               #intialize the list
list2 = []
count=1
while True:                 #generate infinite loop
    n = input("Enter the string :")   
    if not n:               #if input is not present come out of the loop
        break
    list1.append(n)             # if input is there insert the input at the last in list1
for i in list1:                 #extend the each element and store in new list
    list2.extend(i)   
    
for j in list2:             # for each element in list2
    
    if j in dict1.keys():       #if the element in already in dictionary upgrade the value
        
        dict1[j]= dict1[j]+1
    else:                           # if the element not in dictionary intialize the value
        count = 1
        dict1[j]=count
print(dict1)                            #print dictionary in console
   
   
    
    
    