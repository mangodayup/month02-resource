"""
与服务端风格一致
"""
from socket import *

# 服务端地址
ADDR = ("127.0.0.1",8888)

class QueryWord:
    def __init__(self):
        self.sock = socket(AF_INET,SOCK_DGRAM)

    def close(self):
        self.sock.close()

    # 输入输出
    def query_word(self):
        while True:
            word = input("Word:")
            if not word:
                break
            mean = self.get_mean(word)
            print("%s : %s"%(word,mean))

    def get_mean(self,word):
        self.sock.sendto(word.encode(),ADDR)
        mean,addr = self.sock.recvfrom(1024)
        return mean.decode()

if __name__ == '__main__':
    query = QueryWord()
    query.query_word()
    query.close()