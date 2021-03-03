"""
Name : Levi
Email : lvze@tedu.cn
Date : 2021-2-22
Env : Python 3.6

socket and process exercise
"""
from socket import *
from multiprocessing import Process

# 服务端地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 保存用户的字典 {name:address}
user = {}


# 　处理进入聊天室请求
def login(sock, name, address):
    if name in user or "管理" in name:
        sock.sendto(b"FAIL", address)
    else:
        sock.sendto(b"OK", address)
        # 告知其他人
        msg = "欢迎 %s 进入聊天室" % name
        for key, value in user.items():
            sock.sendto(msg.encode(), value)
        user[name] = address  # 存储该用户
        # print(user)  # 测试


# 处理聊天
def chat(sock, name, content):
    msg = "%s : %s" % (name, content)
    for key, value in user.items():
        # 除去本人
        if name != key:
            sock.sendto(msg.encode(), value)


# 处理退出
def exit(sock, name):
    if name in user:
        del user[name]  # 删除用户
    # 通知其他人
    msg = "%s 退出了群聊" % name
    for key, value in user.items():
        sock.sendto(msg.encode(), value)


# 处理客户端请求
def handle(sock):
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
            # tmp --> [EXIT,name]
            exit(sock, tmp[1])


# 入口函数
def main():
    # udp循环网络
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(ADDR)

    # 创建子进程用于处理请求，父进程发送管理员消息
    p = Process(target=handle, args=(sock,), daemon=True)
    p.start()

    while True:
        content = input("管理员消息:")
        if content == 'exit':
            break
        msg = "CHAT 管理员消息 " + content
        # 将消息发送给子进程
        sock.sendto(msg.encode(), ADDR)


if __name__ == '__main__':
    main()  # 启动
