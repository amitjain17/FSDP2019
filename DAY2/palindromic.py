# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:31:51 2019

@author: NITS
"""
r=0
list1 = []                                                      #create list 
list2 =0
n = int(input("Enter the count of number you input in list= "))
for i in range(n):                                      #run loop for creating list
  list_number = int(input("Enter the number="))                   #type number in list
  list1.append(list_number)                                   # enter number in list at last
print(list1)                                    #print list in kernal
for i in list1:                             #access each number in list
  list2 = i
  print(list2)
  while list2>0:                                # if list have positive than perform loop
    d= list2 % 10                               #divide list number with 10 and store remainder
    r=(r*10)+d                                  
    list2=list2 // 10                           #divide the list number with 10
  if i == r:                                    #check number is palindrome or not
    print("number is palindrome  TRUE")
    break
else:
    print("number is not a palindrome   FALSE")
    
    