# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:51:20 2019

@author: NITS
"""
""" Replacing of Characters"""


str1 = "RESTART"
index = str1.find('R')
strr = str1[:index+1] + str1[index+1:].replace('R','$')
print(strr)
