# -*- coding: utf-8 -*-
"""
Created on Thu May 16 23:00:13 2019

@author: NITS
"""

from pandas import DataFrame
import mysql.connector

client = mysql.connector.connect( user='root', password='', host='localhost')
c= client.cursor()
c.execute("DROP DATABASE IF EXISTS Bid_no")
c.execute("CREATE DATABASE Bid_no")
c.execute("USE Bid_no")
c.execute("""CREATE TABLE Bid_nos(BID_NO text,
                                  items text,
                                  Quantity_Required int,
                                  Department_Name_And_Address text,
                                  Start_Date text,
                                  End_Date text)""")