# -*- coding: utf-8 -*-
"""
Created on Sat May 18 00:30:26 2019

@author: NITS
"""

list1 =[]       #intialize the list
i=0             #intialize the counter
while True:
    n = input("Enter the number")   #take input from user
    if not n:
        break
    a = n.split(",")                #split the comma seperated values
for x in a:
    list1.append(int(x))            #insert the value in list
for num in range(len(list1)):       #Run loop upto the length of the list1 
    if list1[num]==13 or list1[num-1]==13:      #if the value or the previous value is equal to 13 than ignore that value and the next value also
        continue     
    else:                           #add the values
        i += list1[num]
print("Sum: ",i)                    #print the sum of values 
