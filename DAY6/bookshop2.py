# -*- coding: utf-8 -*-
"""
Created on Mon May 13 23:54:37 2019

@author: NITS
"""

from functools import reduce             #import reduce 
list1 = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)],    #insert the value in list
        [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
        [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
        [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)]]
list2 =[]

#a =0
#for i in range(len(list1)):
#   a = 0
#   for j in range(1,len(list1[i])):
#        b = list1[i][j][2]*list1[i][j][1]
#        a += b
#   list2.append([list1[i][0],a])
#print(list2)


map1 = list(map(lambda x: [x[0]]+list(map(lambda y:round(y[1]*y[2],3),x[1:] ) ) , list1))   #find the product value
map2 = list(map(lambda x: [x[0],reduce(lambda y,z:round(y+z,3),x[1:])],map1))            
print(list(map2))


