# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:35:42 2019

@author: NITS
"""
albha = "qwertyuioplkjhgfdsazxcvbnm "      #write all alphabet
string =['The quick brown fox jumps over the lazy dog'] #wriie the string
list1=[]                            #create the empty list
n=0                                 #intialize the counter
str1 = "".join(string)              #create a string which have no space
str2 = str1.split()
str3  = "".join(str2)
for num in str3:                    #if there any duplicate in string remove it
    if num not in list1:
        list1.append(num)
for i in list1:                     #check the element if all the alphabet is present or not in string
   for j in i.lower():           
       if i in j:                   #increase the counter when each letter of alphabet is come
          n+=1
          break

if n == 26:                         #if the total alphabet is come than the number is 26 and counter is set on 26
    print('Sentence is pengram')
else:
    print("sentence is not pangram")