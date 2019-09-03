#! /usr/bin/env python3

"""
This part user mysql-connectot to connect to database
"""

import mysql.connector
import datetime
import random

mydb=mysql.connector.connect(
        host="localhost",
        user="felix",
        passwd="123456a",
        database="test_db" #this is optional
        )
print(mydb)

mycursor=mydb.cursor()

"""
#create database and table if not exists
mycursor.execute("CREATE DATABASE test_db")
mycursor.execute(" \
CREATE TABLE students( \
id int auto_increment primary key, \
name nvarchar(256), \
birthday date \
) \
")
"""

sqlInsert = "insert into students(name, birthday) values (%s, %s)"
val=("felix"+str(random.randrange(1,100)), datetime.date(1989,5,26))
mycursor.execute(sqlInsert, val)
mydb.commit()

print(mycursor.rowcount)

bulkVal={('anna{}'.format(x),datetime.date(1987,8,26)) for x in random.sample(range(100,200), 20)}

mycursor.executemany(sqlInsert, bulkVal)
mydb.commit()

print(mycursor.rowcount,"Id is:", mycursor.lastrowid)

mycursor.execute("SELECT * from students")
myresult=mycursor.fetchall()

for x in myresult:
    print(x)

mycursor.execute("select name,birthday from students where name=%s",('felix',))
myresult=mycursor.fetchone()
print(myresult)


mycursor.execute("select name,birthday from students where name like '%7%' \
        order by id desc \
        limit 3 offset 1")

myresult=mycursor.fetchall()
for x in myresult:
    print(x)

mycursor.execute("delete from students where name=%s",('anna105',))
mydb.commit()
print(mycursor.rowcount," rows deleted.")


mycursor.execute("update students set birthday=%s where name=%s",(datetime.date(1987,10,10),'anna195',))
mydb.commit()
print(mycursor.rowcount," rows updated.")

mycursor.execute("select name,birthday from students where name=%s",('anna195',))
myresult=mycursor.fetchall()
print(myresult)

mycursor.execute("drop table if exists students2")
"""
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
"""
