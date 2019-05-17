# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:27:10 2019

@author: NITS
"""

#from collections import OrderedDict

dict1= {}    
# OrderedDict()
while True:
    item = input("Enter the product: ")
    if not item:
        break
    list2 = item.split()
    print(list2)
    product = " ".join(list2[:-1])
    print(product)
    price = int(list2[-1])
    print(price)
    
    if product in dict1:
        dict1[product] = dict1[product] + price
    else:
        dict1[product] = price
        
    # dict1[product] = dict1.get(product,0) + price

print(dict1)