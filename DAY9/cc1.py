# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:17:34 2019

@author: NITS
"""

from pymongo import MongoClient
#from pandas import DataFrame

client = MongoClient("mongodb://amitjain:amitjain17@cluster0-shard-00-00-vbzzs.mongodb.net:27017,cluster0-shard-00-01-vbzzs.mongodb.net:27017,cluster0-shard-00-02-vbzzs.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
mydb = client.student_db

def data(name,age,roll,branch):
    mydb.students.insert_one({"student_name":name,
                              "Student_age":age,
                              "Student_rollno":roll,
                              "Student_branch":branch
            }
            )
    return "student added successfully"

def fetch():
    user = mydb.students.find()
    for i in user:
        print (i)
        
        
data("Amitjain0",20,705,"ECE")
data("Amitjain1",20,705,"ECE")
data("Amitjain2",20,705,"ECE")
data("Amitjain3",20,705,"ECE")
data("Amitjain4",20,705,"ECE")
data("Amitjain5",20,705,"ECE")

fetch()