"""
1. tcp传输
2. 连续循环快速发送
"""

from socket import *
from time import sleep

names = [
    "Lily",
    "Lucy",
    "Tom",
    "Jame"
]

def main():
    sock = socket()
    sock.connect(("127.0.0.1",8887))

    # 设置# 为名字分割符号
    name = "#".join(names)
    sock.send(name.encode())

    # 接受结果
    result = sock.recv(1024).decode()
    print(result)
    sock.close()


# def main():
#     sock = socket()
#     sock.connect(("127.0.0.1",8887))
#     # 循环发送名字
#     for name in names:
#         sock.send(name.encode())
#         sleep(0.1) # 控制速度
#     sock.send(b"##") # 让服务端结束
#     # 接受结果
#     result = sock.recv(1024).decode()
#     print(result)
#     sock.close()

if __name__ == '__main__':
    main()
