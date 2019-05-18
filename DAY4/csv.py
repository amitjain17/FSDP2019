# -*- coding: utf-8 -*-
"""
Created on Sat May 18 13:03:32 2019

@author: NITS
"""
import csv                               #import the csv library
with open("passwd") as pas:             #open the file passwd
    with open("etc.csv",'w') as etc:        #create the csv file name etc
        new = csv.reader(pas,delimiter=":")     #read each element with delimiter=":"
        for row in new:                         #write each information in etc file
            etc.writelines([row[0],"  ",row[2],'\n'])
            
