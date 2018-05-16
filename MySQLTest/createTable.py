#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost", "root", "root", "pythonmysqltest")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS PythonTest")

sql = """CREATE TABLE PythonTest(
        `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
        `name` varchar(255) NOT NULL DEFAULT '',
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB CHARSET=utf8mb4
      """
cursor.execute(sql)

db.close()