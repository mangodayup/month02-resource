"""
数据库操作  连接和断开
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

# 对数据进行 读写操作

# 关闭数据库连接
cur.close()
db.close()
