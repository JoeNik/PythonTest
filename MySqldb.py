import MySQLdb

db = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='1', db='mysql', charset='utf8')

cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT * FROM tb_test")

# 使用 fetchall() 方法获取s所有数据.
data = cursor.fetchall()
print(data)

cursor.close()
db.close()

