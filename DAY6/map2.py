# -*- coding: utf-8 -*-
"""
Created on Mon May 13 22:06:30 2019

@author: NITS
"""

names = ['Mary', 'Isla', 'Sam']

"""WAY1"""

#for i in range(len(names)):
#    names[i] = hash(names[i])


"""WAY 2"""

#def has(n):
#  for i in range(len(names)):
#   return hash(names[i])
#map1 = map(has,names)
#print(list(map1))




"""WAY 3"""

map1 = map(hash,names)              #using list comprehence call the hash function in names list     
print(list(map1))                   #display the list map1
