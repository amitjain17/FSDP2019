# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:18:07 2019

@author: NITS
"""
import json

with open("faculty.json","r") as fac:
    fac1 = json.load(fac)
    print(fac1)
    
