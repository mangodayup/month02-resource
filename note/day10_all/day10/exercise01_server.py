"""
练习2： 基于dict数据库中的words表完成
从客户端输入单词，发送给服务端，得到单词的
解释，并打印出来
接收单词 --》 查询单词解释 --》 发送单词解释
"""
from socket import *
import pymysql


# 　数据库处理
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

    # 查询单词
    def get_mean(self, word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql, [word])
        mean = self.cur.fetchone()  # (mean,) None
        if mean:
            return mean[0]
        else:
            return "Not Found"


# 　网络搭建
class QueryWord:
    def __init__(self, host="0.0.0.0", port=8000):
        self.host = host
        self.port = port
        self.dict = Dict()  # 实例化数据库对象
        self.sock = self.__create_socket()

    def __create_socket(self):
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.bind((self.host, self.port))
        return sock

    def close(self):
        self.sock.close()
        self.dict.close()

    # 　查询单词
    def query_word(self):
        while True:
            word, addr = self.sock.recvfrom(128)
            # 查询单词 (使用数据库)
            mean = self.dict.get_mean(word.decode())
            self.sock.sendto(mean.encode(), addr)


if __name__ == '__main__':
    query = QueryWord(host="0.0.0.0", port=8888)
    query.query_word()  # 具体逻辑任务
    query.close()
