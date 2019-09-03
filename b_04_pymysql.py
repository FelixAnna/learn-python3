#! /usr/bin/env python3

"""
This part shows you
how to connect to mysql with PyMySQL
"""

import pymysql

db=pymysql.connect("localhost",'felix','123456a','test_db')

cursor=db.cursor()

cursor.execute("select version()")
print(cursor.fetchone())


#create table

cursor.execute("drop table if exists employees")
cursor.execute("create table employees( \
        id int auto_increment primary key, \
        name nvarchar(256), \
        birthday datetime \
        )")

#insert record
import datetime
try:
    cursor.execute("insert into employees(name,birthday) values('%s','%s')" % ('felix',datetime.date(1989,7,11)))
    db.commit()
except:
    db.rollback()

#query record

cursor.execute("select * from employees where name='%s'" %('felix',))
for x in cursor.fetchall():
    print(x)

#update record
try:
    cursor.execute("update employees set birthday='%s' where name='%s'"%(datetime.date(1989,7,11),'felix'))
    db.commit()
except:
    db.rollback()

#delete record

try:
    cursor.execute("delete from employees set where name='%s'"%('felix',))
    db.commit()
except:
    db.rollback()

db.close()
