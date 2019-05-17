# -*- coding: utf-8 -*-
"""
Created on Mon May 13 22:06:30 2019

@author: NITS
"""

names = ['Mary', 'Isla', 'Sam']

#for i in range(len(names)):
#    names[i] = hash(names[i])


def has(n):
  for i in range(len(names)):
   return hash(names[i])
map1 = map(has,names)
print(list(map1))




map1 = map(hash,names)
print(list(map1))
