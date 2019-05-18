# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:50:21 2019

@author: NITS
"""
import csv
with open("zoo.csv") as zoo1:               #import csv file
  #  print(zoo1.readlines())
    zoo2 = csv.reader(zoo1,delimiter=",")     #read each and every line in the csv file
    for row in zoo2:
       print(row)

#{"elephant":[[1001,1002,1003],[500,600,550]],"tiger":[[],[]],}

animal_data = {}                            #intialize the dictionary
with open("zoo.csv") as zoo1:               #open csv file
    zoo2 = csv.reader(zoo1,delimiter=",")
    next(zoo2)                              #skip the first line
    for row in zoo2:
        if row[0] not in animal_data:             
            animal_data[row[0]] = [[int(row[1])],[int(row[2])]]
        else:
            animal_data[row[0]][0].append(int(row[1]))
            animal_data[row[0]][1].append(int(row[2]))
print(animal_data)

sum(animal_data["elephant"][1])