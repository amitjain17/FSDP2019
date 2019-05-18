# -*- coding: utf-8 -*-
"""
Created on Wed May  8 22:55:53 2019

@author: NITS
"""
def reverse(x):
    #reverse_String[::-1]
    return (x[ : :-1])    #splicing the string


n = str(input("Enter the string"))
print(reverse(n))

