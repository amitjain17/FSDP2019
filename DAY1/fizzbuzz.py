# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:50:31 2019

@author: NITS
"""

"""FIZZBUZZ"""

i=1
while i <=100:                          #
    if i%3 == 0 and i%5==0:
        print("FIZZBUZZ")
        i+=1
        continue
    if i%3 == 0:
        print("Fizz")
        i+=1
        continue
    if i%5 == 0:
        print("Buzz")
        i+=1
        continue
    if i%3 !=0 and i%5 !=0:
        print(i)
        i+=1
        continue
        