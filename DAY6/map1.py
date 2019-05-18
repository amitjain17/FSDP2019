# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:38:05 2019

@author: NITS
"""

import random                                         #intialize the random function

names = ['Mary', 'Isla', 'Sam']                  #create the list
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']     #create the list for code_names


#for i in range(len(names)):
#    names[i] = random.choice(code_names)
    
#print (names)


#
#def ra(names,code_names):
#    for i in range(len(names)):
#        names[i] = random.choice(code_names)
        
names = map(lambda x: random.choice(code_names), names)   #using list comprehence assign code name to every name
print(list(names))
