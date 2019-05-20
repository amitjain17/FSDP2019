# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:04:50 2019

@author: NITS
"""
import numpy as np                      #import numpy
import matplotlib.pyplot as plt
                            #mean #s.d. #variance
incomes = np.random.normal(100.0, 20.0,10000)                         #create normal distribution value
print("Mean: ",np.mean(incomes))                         #find mean of given value
print("Median:",np.median(incomes))                        #find median of given value
#plt.hist(incomes)

inc = np.random.randint(300,500,500)            #generate random value in between 300to 500
inc = np.append(incomes,inc)                     #append the new value in inc
mean =int(np.mean(inc))                               #find mean of inc
std = int(np.std(inc))                          #find standared deviation of inc
vari =int(np.var(inc))                          #find variance of inc
new  = np.random.normal(mean,std,vari)
plt.hist(new)                                    #plot the histogram         


