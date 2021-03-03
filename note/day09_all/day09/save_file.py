"""
二进制数据存储
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

# 写入二进制文件
# with open('ch.jpg','rb') as f:
#     data = f.read()
# sql = "update class set image=%s where id=1;"
# cur.execute(sql,[data])
# db.commit()

# 提取二进制文件
sql = "select image from class where name='Lily';"
cur.execute(sql)
result = cur.fetchone() # (image,)
with open("采花.jpg",'wb') as f:
    f.write(result[0])



# 关闭数据库连接
cur.close()
db.close()