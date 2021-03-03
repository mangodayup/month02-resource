from socket import *

# 服务器地址
server_address = ("127.0.0.1",8888)

tcp_socket = socket()
tcp_socket.connect(server_address)
while True:
    msg = input(">>")
    # 直接客户端退出
    if not msg:
        break
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print(data.decode())

tcp_socket.close()




