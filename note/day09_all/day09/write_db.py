"""
数据库操作  写数据库

innodb引擎支持事务 必须提交才能生效
myisam引擎不支持事务 执行execute后直接生效
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

# 对数据进行写操作 正删改
name = input("姓名:")
score = input("分数:")
try:
    # sql = "update class set score=91 where id=1;"
    sql = "update class set score=%s " \
          "where name=%s;"
    # print(sql)
    cur.execute(sql,[score,name]) # 执行语句
    db.commit() # 提交事务
except Exception as e:
    print(e)
    db.rollback() # 回滚

# 关闭数据库连接
cur.close()
db.close()
