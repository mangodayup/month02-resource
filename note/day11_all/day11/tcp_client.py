"""
tcp 客户端流程
重点代码 ！！
"""
from socket import *

# 服务器地址
server_address = ("127.0.0.1",8888)

# 使用默认参数就是tcp套接字
tcp_socket = socket()

# 发起连接
tcp_socket.connect(server_address)

# 发送接收消息
while True:
    msg = input(">>")
    # 直接客户端退出
    # if not msg:
    #     break

    tcp_socket.send(msg.encode())
    # 退出标志
    if msg == '##':
        break
    data = tcp_socket.recv(1024)
    print("从服务端收到:",data.decode())

tcp_socket.close()




