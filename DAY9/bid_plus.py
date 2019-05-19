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
c.execute("INSERT INTO Bid_nos VALUES(123,'a_item',2, 'x_department','19 May 2019','20 May 2019')")
c.execute("INSERT INTO Bid_nos VALUES(456,'b_item',3, 'y_department','19 May 2019','20 May 2019')")
c.execute("INSERT INTO Bid_nos VALUES(789,'c_item',4, 'z_department','19 May 2019','20 May 2019')")
c.execute("INSERT INTO Bid_nos VALUES(159,'d_item',5, 'm_department','19 May 2019','20 May 2019')")

c.execute("SELECT * FROM Bid_nos")
db = DataFrame(c.fetchall())
db.columns = ["BID_NO","ITEMS","QUANTITY","DEPARTMENT","START_NAME","END_DATE"]
print(db)
client.commit()
client.close()