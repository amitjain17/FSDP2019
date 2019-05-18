# -*- coding: utf-8 -*-
"""
Created on Wed May  8 23:39:04 2019

@author: NITS
"""
vowels = ['a','e','i','o','u',' ','A','E','I','O','U'] 
def translate(a):
    #list1 = []
    for i in a:
        list2 =[]                                        #intialize the list
        for j in i:
            if j not in vowels:
                
                list2.append(j+"o"+j)                    #change the string in another format if the string character is vowel
            else:
                list2.append(j)                         #insert the character in the list if it is not vowel
        #list1.append(''.join(list2))        
        s=''.join(list2)
    print(s)       
            
    
    

list1 = []
n = input("Enter the string")                       #enter the string
list1.append(n)                     #insert the string in list1
translate(list1)                    #call the function translate
    