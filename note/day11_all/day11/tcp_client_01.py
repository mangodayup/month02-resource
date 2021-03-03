"""
tcp 客户端流程
每次访问服务端都重新建立连接
"""
from socket import *

# 服务器地址
server_address = ("127.0.0.1",8888)

while True:
    msg = input(">>")
    if not msg:
        break

    tcp_socket = socket()
    tcp_socket.connect(server_address)
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("从服务端收到:",data.decode())
    tcp_socket.close()




