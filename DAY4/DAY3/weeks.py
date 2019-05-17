# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:49:03 2019

@author: NITS
"""

tuple1 = ('Monday','Tuesday','Friday')
enum = ('Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday','Sunday')
#dict1 = {'Monday':1,'Tuesday':2,'Wednesday':3,'Thrusday':4,'Friday':5,'Saturday':6,'Sunday':7}
a= enumerate(enum)

for k,y in a:
    print("{},{}".format(k,y))
    
new_t = (tuple1[:2]+("Wednesday","Thursday")+(tuple1[-1],)+("Saturday","Sunday"))
print(new_t)
"""

l = []

for i in enum:
    if i not in tuple1:
        l.append(i)
    else:
        l.append(i)
print(tuple(l))"""