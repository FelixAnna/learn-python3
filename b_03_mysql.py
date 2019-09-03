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

cursor=mydb.cursor()

"""
#create database and table if not exists
cursor.execute("CREATE DATABASE test_db")
cursor.execute(" \
CREATE TABLE students( \
id int auto_increment primary key, \
name nvarchar(256), \
birthday date \
) \
")
"""

sqlInsert = "insert into students(name, birthday) values (%s, %s)"
val=("felix"+str(random.randrange(1,100)), datetime.date(1989,5,26))
cursor.execute(sqlInsert, val)
mydb.commit()

print(cursor.rowcount)

bulkVal={('anna{}'.format(x),datetime.date(1987,8,26)) for x in random.sample(range(100,200), 20)}

cursor.executemany(sqlInsert, bulkVal)
mydb.commit()

print(cursor.rowcount,"Id is:", cursor.lastrowid)

cursor.execute("SELECT * from students")
myresult=cursor.fetchall()

for x in myresult:
    print(x)

cursor.execute("select name,birthday from students where name=%s",('felix',))
myresult=cursor.fetchone()
print(myresult)


cursor.execute("select name,birthday from students where name like '%7%' \
        order by id desc \
        limit 3 offset 1")

myresult=cursor.fetchall()
for x in myresult:
    print(x)

cursor.execute("delete from students where name=%s",('anna105',))
mydb.commit()
print(cursor.rowcount," rows deleted.")


cursor.execute("update students set birthday=%s where name=%s",(datetime.date(1987,10,10),'anna195',))
mydb.commit()
print(cursor.rowcount," rows updated.")

cursor.execute("select name,birthday from students where name=%s",('anna195',))
myresult=cursor.fetchall()
print(myresult)

cursor.execute("drop table if exists students2")
"""
cursor.execute("SHOW DATABASES")

for x in cursor:
    print(x)
"""
