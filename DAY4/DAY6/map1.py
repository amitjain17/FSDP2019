# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:38:05 2019

@author: NITS
"""

import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']


#for i in range(len(names)):
#    names[i] = random.choice(code_names)
    
#print (names)


#
#def ra(names,code_names):
#    for i in range(len(names)):
#        names[i] = random.choice(code_names)
        
names = map(lambda x: random.choice(code_names), names)
print(list(names))
