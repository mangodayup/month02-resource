"""
批量写操作
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

# 对数据写操作
data = [
    ("Lucy",18,'w',76),
    ("Joy",17,'m',69),
    ("Levi",18,'m',81)
]
sql = "insert into class (name,age,sex,score) " \
      "values (%s,%s,%s,%s);"
cur.executemany(sql,data)
db.commit()


# 关闭数据库连接
cur.close()
db.close()
