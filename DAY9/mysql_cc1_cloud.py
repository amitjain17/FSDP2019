# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:22:02 2019

@author: NITS
"""
import mysql.connector
from pandas import DataFrame

client= mysql.connector.connect(user= 'user_st',password='password',
                                host='db4free.net',database='database_st')
c = client.cursor()
c.execute("DROP DATABASE IF EXISTS database_st;")

c.execute("CREATE DATABASE database_st;")

c.execute("USE database_st")
#c.execute("DROP Table database_st;")

c.execute("""CREATE TABLE database_st(SNAME text,
                                      ROLL_NO int,
                                      BRANCH text,
                                      STUDENT_AGE int)""")
  
  
c.execute("INSERT INTO database_st VALUES('Amit0',705,'ECE',20)")
c.execute("INSERT INTO database_st VALUES('Amit1',705,'ECE',20)")
c.execute("INSERT INTO database_st VALUES('Amit2',705,'ECE',20)")
c.execute("INSERT INTO database_st VALUES('Amit3',705,'ECE',20)")

c.execute("""SELECT * FROM database_st""")
db = DataFrame(c.fetchall())

db.columns = ["Name","Roll_no","Branch","Age"]
print(db)
