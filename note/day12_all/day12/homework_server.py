"""
使用tcp完成一个会话小程序

问答小字典
{"key":"value",........}
key: 几岁
value : 我两岁了

从客户端 发送个问题给服务端，服务端根据
字典比对关键词回复问题，客户端收到回复
打印。
如果问题无法回复，统一回答 "人家还小不知道啦"
"""
from socket import *

# 对话字典
chat = {
    "你好": "你好啊！",
    "叫什么": "我叫小美，是机器人",
    "男生女生": "我是机器人，没有性别",
    "你几岁": "我2岁啦"
}


def handle(connfd):
    # 接收问题
    q = connfd.recv(1024).decode()
    for key in chat:
        if key in q:
            connfd.send(chat[key].encode())
            break
    else:
        connfd.send("人家还小不知道啦".encode())


def main():
    sock = socket()
    sock.bind(("0.0.0.0", 8888))
    sock.listen(5)
    # 循环处理对话
    while True:
        connfd, addr = sock.accept()
        handle(connfd)  # 处理对话
        connfd.close()

if __name__ == '__main__':
    main()