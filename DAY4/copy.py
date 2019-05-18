# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:50:35 2019

@author: NITS
"""
with open("new.txt",'rt') as fp:                    #open the file in which data is present
    with open("new3.txt",'w') as fp1:               #open another file in which we have to copy the data
        for item in fp.readlines():                      #read each line in file 1 and copy in another file
            fp1.write(item) 
            
with open("new3.txt",'rt') as fp1:                 #print the file in console
    print(fp1.read())
    
    

    
    
    
    
    
    
    
    
    
    
    