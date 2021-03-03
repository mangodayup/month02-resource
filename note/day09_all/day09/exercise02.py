"""
练习02： 编写一个类，类中提供两个方法
分别是注册（要求用户名不能重复）和登录方法
在books中创建 user表 ： id  user password
create table user (
id int primary key auto_increment,
user char(50) not null unique,
password char(64)
);

注册： 要求写入用户名密码
登录 : 验证用名和密码
返回布尔值表达 成功或者失败
"""

import pymysql

class User:
    def __init__(self):
        self.kwargs = {
            "user": "root",
            "password": "123456",
            "database": "books",
            "charset": "utf8"
        }
        self.__connect()

    # 完成链接数据库
    def __connect(self):
        self.db = pymysql.connect(**self.kwargs)
        self.cur = self.db.cursor()

    # 关闭
    def close(self):
        self.cur.close()
        self.db.close()

    # 注册方法
    def register(self,user,passwd):
        try:
            sql = "insert into user (user,password) values (%s,%s);"
            self.cur.execute(sql,[user,passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    # 登录
    def login(self, user, passwd):
        sql = "select user from user where user=%s and password=%s;"
        self.cur.execute(sql,[user,passwd])
        if self.cur.fetchone():
            return True
        else:
            return False


if __name__ == '__main__':
    user = User()

    if user.login("Tom",'1230'):
        print("登录成功")
    else:
        print("登录失败")

    # if user.register("Tom",'123'):
    #     print("注册成功")
    # else:
    #     print("注册失败")