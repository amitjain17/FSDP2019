# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:27:10 2019

@author: NITS
"""

#from collections import OrderedDict

dict1= {}                           #intialize the dictionary
# OrderedDict()
while True:
    item = input("Enter the product and price: ")       #Enter the input from user
    if not item:
        break
    list2 = item.split()
    print(list2)
    product = " ".join(list2[:-1])                      #find the product from given infromation
    print(product)
    price = int(list2[-1])                      #find the price from given information
    print(price)
    
    if product in dict1:                            #if the product in dictionary update the price
        dict1[product] = dict1[product] + price
    else:
        dict1[product] = price                          #else intialize the price in dictionary
        
    # dict1[product] = dict1.get(product,0) + price

print(dict1)