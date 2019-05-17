# -*- coding: utf-8 -*-
"""
Created on Mon May 13 23:35:36 2019

@author: NITS
"""
list1 = [   [34587, 'Learning Python, Mark Lutz' , 4, 40.95],
    [98762, 'Programming Python, Mark Lutz' ,5, 56.80],
    [77226,' Head First Python, Paul Barry ',3, 32.95],
    [88112, 'Einführung in Python3, Bernd Klein',3, 24.99]]
#list2=[]
#for item in list1:
#    order_number= item[0]
#    total_price= item[2]*item[3]
#    if total_price<=100:
#        total_price = total_price + 10
#    list2.append((order_number,total_price))
#print(list2)




min_value=100   
map1 = map(lambda x: [x[0],round(x[2]*x[3],2)],list1)
                    #new = list(map1)
map2 = map(lambda y: (y[0],y[1]+10)  if y[1]<=min_value else tuple(y),list(map1))
print(list(map2))
#map2 = map(lambda y: tuple(y) if y[1]>=min_value else (y[0],y[1]+10) ,list(map1))


    
    
