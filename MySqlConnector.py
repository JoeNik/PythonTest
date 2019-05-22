#!/usr/bin/python3

import mysql.connector

# 打开数据库连接
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1",
  database="mysql"
)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT * FROM tb_test")

# 使用 fetchall() 方法获取s所有数据
data = cursor.fetchall()

print(data)

# 关闭数据库连接
db.close()

