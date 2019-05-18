# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:50:31 2019

@author: NITS
"""

"""FIZZBUZZ"""

i=1                                         #intialize the counter
while i <=100:                          #start the loop from 1 to 100
    if i%3 == 0 and i%5==0:             #if the number is divided by 3 and 5 print FIZZBUZZ
        print("FIZZBUZZ")
        i+=1
        continue
    if i%3 == 0:                      #if the number is divided by 3 then print Fizz
        print("Fizz")
        i+=1
        continue
    if i%5 == 0:                        #if the number is divided by 5 the print Buzz
        print("Buzz")
        i+=1
        continue
    if i%3 !=0 and i%5 !=0:            #if the number is not divided by 3 and 5 then print the number 
        print(i)
        i+=1
        continue
        