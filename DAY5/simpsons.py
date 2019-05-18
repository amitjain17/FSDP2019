# -*- coding: utf-8 -*-
"""
Created on Sat May 11 21:38:32 2019

@author: NITS
"""
import re                                  #import regular expression
list3 =[]                                  #intialize the list
with open("simpsons_phone_book.txt",'rt') as simp:     #open the text file
    list1 = simp.read()
    list2 = list1.split("\n")
    for item in list2:                        #search for the name in the file
        if re.search(r'^[j|J]{1}[Neu]',item):
            list3.append(item)
for i in list3:  
 print(i)
    