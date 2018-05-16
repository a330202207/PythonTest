#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost", "root", "root", "pythonmysqltest")

cursor = db.cursor()

cursor.execute("set names utf8")

# sql = "INSERT INTO PythonTest (name) VALUES ('张三')"


name = '李四'

sql = "INSERT INTO PythonTest(name) VALUES ('%s')" % (name)

try:
    cursor.execute(sql.encode('utf8'))
    db.commit()
except:
    print('错误')
    db.rollback()

db.close()