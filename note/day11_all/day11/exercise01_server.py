"""
练习02：
从客户端，将一个图片发送到服务端存储
图片自选，服务端将图片存储为 "20210219.jpg"

思路提示： 客户端  读取 --》 发送
          服务端  接收 --》 写入
"""

from socket import *

# 接收文件
def recv_file(connfd):
    file = open("20210219.jpg",'wb')
    # 边接收边写入
    while True:
        data = connfd.recv(1024) # 文件内容
        if not data:
            break
        file.write(data)
    file.close()

def main():
    # 创建tcp套接字
    tcp_socket = socket()
    tcp_socket.bind(("0.0.0.0",8888))
    tcp_socket.listen(5)

    # 处理客户端连接
    connfd,addr = tcp_socket.accept()
    print("Connect from",addr)
    # 接收文件
    recv_file(connfd)
    connfd.close()

if __name__ == '__main__':
    main()










