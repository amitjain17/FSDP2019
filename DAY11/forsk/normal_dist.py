# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:40:16 2019

@author: NITS
"""

import numpy as np
import matplotlib.pyplot as plt

value = np.random.normal(150,20,1000)                #create random normal number
print("Standared_deviation:",np.std(value))         #find the standard deviation and print it
print("Variance:",np.var(value))                    #find the variance and print it

plt.hist(value,100)          #print the histogram with bucket size 100