"""
数据库 查询操作
"""
import pymysql

args = {
    "host": "172.40.91.124",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "stu",
    "charset": "utf8"
}

# 连接数据库
db = pymysql.connect(**args)

# 创建游标 游标是操作数据，得到操作结果的对象
cur = db.cursor()

# 对数据进行读操作
sql = "select name,age,score from " \
      "class where score>%s;"
cur.execute(sql,[85])

# 执行查询后，游标是一个可迭代对象
for row in cur:
    print(row) # 一条记录

# 取出第一个查询结果  None
# one = cur.fetchone()
# print(one)

# 取出剩下的前2个查询结果  ()
# many = cur.fetchmany(2)
# print(many)

# 取出所有查询结果  ()
# all = cur.fetchall()
# print(all)

# 关闭数据库连接
cur.close()
db.close()