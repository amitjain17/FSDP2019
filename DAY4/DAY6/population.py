# -*- coding: utf-8 -*-
"""
Created on Wed May 15 00:52:57 2019

@author: NITS
"""
import csv
with open("population.csv") as popu:
   # new = csv.reader(popu,delimiter = ",")
    new1 = csv.DictReader(popu)
    for item in new1:
        print(dict(item))
        