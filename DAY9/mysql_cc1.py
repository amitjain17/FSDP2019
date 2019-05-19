# -*- coding: utf-8 -*-
"""
Created on Sun May 19 19:38:07 2019

@author: NITS
"""

import mysql.connector
from pandas import DataFrame

conn = mysql.connector.connect(user='root', password='', host='localhost')

c = conn.cursor()
c.execute("DROP DATABASE IF EXISTS student2;")
c.execute("CREATE DATABASE student2;")
c.execute("USE student2;")
c.execute("""CREATE TABLE student2(student_name TEXT,
                                  student_roll_no INTEGER,
                                  student_branch TEXT,
                                  student_age INTEGER
        )
        """)
c.execute("""INSERT INTO student2 VALUES ('Amit0',705,'ECE',20)""" )
c.execute("""INSERT INTO student2 VALUES ('Amit1',705,'ECE',20)""" )
c.execute("""INSERT INTO student2 VALUES ('Amit2',705,'ECE',20)""" )

c.execute("""SELECT * FROM student2""")
db = DataFrame(c.fetchall())

db.columns = ["Name","Roll_no","Branch","Age"]
print(db)
conn.commit()
conn.close()