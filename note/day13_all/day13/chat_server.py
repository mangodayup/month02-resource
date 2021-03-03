"""
Name : Levi
Email : lvze@tedu.cn
Date : 2021-2-22
Env : Python 3.6

socket and process exercise
"""
from socket import *

# 服务端地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 保存用户的字典 {name:address}
user = {}


# 　处理进入聊天室请求
def login(sock, name, address):
    if name in user:
        sock.sendto(b"FAIL", address)
    else:
        sock.sendto(b"OK", address)
        # 告知其他人
        msg = "欢迎 %s 进入聊天室" % name
        for key, value in user.items():
            sock.sendto(msg.encode(), value)
        user[name] = address  # 存储该用户
        print(user)  # 测试


# 处理聊天
def chat(sock, name, content):
    msg = "%s : %s" % (name, content)
    for key, value in user.items():
        # 除去本人
        if name != key:
            sock.sendto(msg.encode(), value)


# 处理退出
def exit():
    pass


# 入口函数
def main():
    # udp循环网络
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(ADDR)

    # 循环接收各个客户端消息
    while True:
        request, addr = sock.recvfrom(1024)
        tmp = request.decode().split(' ', 2)  # 简单解析请求
        if tmp[0] == "LOGIN":
            # tmp--> [LOGIN,name]
            login(sock, tmp[1], addr)
        elif tmp[0] == "CHAT":
            # tmp --> [CHAT,name,content]
            chat(sock, tmp[1], tmp[2])
        elif tmp[0] == "EXIT":
            exit()


if __name__ == '__main__':
    main()  # 启动
