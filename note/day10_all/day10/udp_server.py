"""
udp_server.py
udp 服务端 示例代码
重点代码 ！！！
"""
from socket import *

# 创建udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
udp_socket.bind(("0.0.0.0",8888))

while True:
    # 接收消息 data-->bytes
    data,addr = udp_socket.recvfrom(5)
    # 客户端随服务端结束
    # if not data:
    #     break
    print("从",addr,"收到:",data.decode())

    # 发送消息 发给刚才的地址
    udp_socket.sendto(b"Thanks",addr)

# 关闭套接字
udp_socket.close()










