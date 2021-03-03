"""
练习04：
有一个列表，列表中有一些名字，将这些名字
从客户端发送给服务端，如果名字里有 “张三”
则服务端返回一个 "存在VIP" 如果没有则
返回 "不存在VIP"
"""
from socket import *

def vip(connfd):
    name = connfd.recv(1024).decode()
    names = name.split('#')
    if "Tom" in names:
        connfd.send("存在vip".encode())
    else:
        connfd.send("不存在vip".encode())


# def vip(connfd):
#     flag = False # 标志位
#     while True:
#         name = connfd.recv(1024).decode()
#         if name == "Tom":
#             flag = True
#         elif name == "##":
#             break
#
#     if flag:
#         connfd.send("存在VIP".encode())
#     else:
#         connfd.send("不存在VIP".encode())

def main():
    # tcp 套接字
    sock = socket()
    sock.bind(("0.0.0.0",8887))
    sock.listen(5)
    connfd,addr = sock.accept()
    vip(connfd) # 判断是否有vip
    connfd.close()

if __name__ == '__main__':
    main()
