# -*- coding: utf-8 -*-
"""
Created on Mon May 13 22:41:06 2019

@author: NITS
"""

from functools import reduce

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

#height_total = 0
#height_count = 0
#for person in people:
#    if 'height' in person:
#        height_total += person['height']
#        height_count += 1
#
#if height_count > 0:
#    average_height = height_total / height_count
#
#    print (average_height)
    
#Try rewriting the code below using map, reduce and filter. 
#Filter takes a function and a collection. 
#It returns a collection of every item for which the function returned True.
    

fill= map(lambda y: y['height'] ,filter(lambda x: 'height' in x ,people))
a = list(fill)
value = reduce(lambda x,y:x+y,a) / len(list(a))
print(value)
    
