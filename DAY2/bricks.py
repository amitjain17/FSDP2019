# -*- coding: utf-8 -*-
"""
Created on Wed May  8 22:29:04 2019

@author: NITS
"""

def bricks(a,b,c):                                      #create function name bricks
    size = (a*1)+(b*5)                                  #find the total size of bricks cover
    if c <= size:                           #check wheateher the total size is complete our requirment
        return True
    else:
        return False
small_brick_size = int(input("Enter the number of small brick"))  #input small brick number
large_brick_size = int(input("Enter the number of large brick"))    #input large brick number
total_area = int(input("ENter the total area"))                 #total covered area
print(bricks(small_brick_size,large_brick_size,total_area)) #call function