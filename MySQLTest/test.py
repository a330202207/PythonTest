#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost", "root", "root", "pythonmysqltest")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version : %s " % data)
