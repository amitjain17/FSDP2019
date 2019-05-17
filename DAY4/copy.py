# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:50:35 2019

@author: NITS
"""
with open("new.txt",'rt') as fp:
    with open("new3.txt",'w') as fp1:
        for item in fp.read():
            fp1.write(item)
            
with open("new3.txt",'rt') as fp1:    
    print(fp1.read())
    
    

    
    
    
    
    
    
    
    
    
    
    