# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:37:11 2019

@author: NITS
"""
"""Weighted score calculator"""



weighted_score = 0
A1 = int(input("Enter the marks of Asssigment 1"))  #marks of Assigment1
A2 = int(input("Enter the marks of Asssigment 2"))  #marks of Assigment2
A3 = int(input("Enter the marks of Asssigment 3"))  #marks of Assigment3
E1 = int(input("Enter the marks of Exam1"))         #Exam marks1
E2 = int(input("Enter the marks of Exam2"))         #Exam marks2

weighted_score = (( A1 + A2 + A3 ) *0.1) + ((E1 + E2 ) * 0.35)  #Weight value
print('weighted score=',weighted_score)             #print weight value

