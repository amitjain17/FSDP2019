# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:12:19 2019

@author: NITS
"""

import pandas as pd
import numpy as np                      

df = pd.read_csv("Automobile.csv")                   #read the csv file using pandas
df1 = df[(df['price'] < 11000)]                     #remove the outlayer from the dataframe file                      
df['price'] = df['price'].fillna(int(df1['price'].mean()))  #find the mean of the file and insert at the place where NAN value will be shown
arr  = np.array(df1['price'])                           #convert the dataframe coloumn into ndarray
arr1 = np.array(df['price'])                            #convert the dataframe coloumn into ndarray
print("Minimum_price :",arr1.min())                        #find the minimum value in nd array and print it
print("Maximum_price :",arr1.max())                     #find the maximum value in nd array and print it
print("Average_price :",arr.mean())                  #use the value of previous price data for findind the accurate mean
print("Standared_deviation:",arr1.std())            #find the standared deviation from ndarray and print it