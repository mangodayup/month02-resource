"""
练习： 创建一个数据库 dict 使用utf8格式
在该数据库下创建一个数据表words
id  word  mean 三个字段

create table words (
id int primary key auto_increment,
word varchar(30),
mean varchar(512));

将单词本 dict.txt 中的单词插入到该数据表
"""
import pymysql
import re


class Dict:
    def __init__(self):
        self.kwargs = {
            "user": "root",
            "password": "123456",
            "database": "dict",
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

    def get_data(self, filename):
        file = open(filename)
        # 组织单词数据 [(word,mean),...]
        words = []
        for line in file:
            word = re.findall(r"(\w+)\s+(.*)", line)
            words += word
        file.close()
        return words

    def insert_words(self, filename):
        data = self.get_data(filename)
        try:
            sql = "insert into words (word,mean) values (%s,%s);"
            self.cur.executemany(sql, data)
            self.db.commit()
        except:
            self.db.rollback()


if __name__ == '__main__':
    dict = Dict()
    # 单词插入
    dict.insert_words("dict.txt")
    dict.close()
