# -*- coding: utf-8 -*-
"""
Created on Sun May 19 19:06:06 2019

@author: NITS
"""

import sqlite3
from pandas import DataFrame
  
conn = sqlite3.connect("student1.db")
c = conn.cursor()
c.execute("""DROP TABLE IF EXISTS student1""")
c.execute("""CREATE TABLE student1(student_name TEXT,
                                  student_roll_no INTEGER,
                                  student_branch TEXT,
                                  student_age
        )
        """)
c.execute("""INSERT INTO student1 VALUES ('Amit',705,'ECE',20)""" )
c.execute("""INSERT INTO student1 VALUES ('Amit1',705,'ECE',20)""" )
c.execute("""INSERT INTO student1 VALUES ('Amit2',705,'ECE',20)""" )

c.execute("""SELECT * FROM student1""")
db = DataFrame(c.fetchall())

db.columns = ["Name","Roll_no","Branch","Age"]
print(db)
conn.commit()
conn.close()