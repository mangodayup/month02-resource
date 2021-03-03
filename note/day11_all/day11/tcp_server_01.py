"""
tcp服务端 同时处理多个客户端
"""
from socket import *

# 创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)
tcp_socket.bind(("0.0.0.0",8888))
tcp_socket.listen(5)

# 每次接收一个消息都要 连接--断开
while True:
    # 等待处理客户端连接
    connfd,addr = tcp_socket.accept()
    data = connfd.recv(1024)
    print("收到:",data.decode())
    connfd.send(b"Thanks")
    connfd.close()

# 关闭套接字
tcp_socket.close()






