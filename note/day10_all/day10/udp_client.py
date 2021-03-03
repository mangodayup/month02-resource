"""
udp_client.py
udp 套接字客户端流程
重点代码 ！！
"""
from socket import *

# 服务器地址
ADDR = ("172.40.91.124",8888)

# 创建udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

while True:
    # 发送输入的内容
    msg = input(">>")
    # 直接退出，不影响服务端
    if not msg:
        break
    udp_socket.sendto(msg.encode(),ADDR)
    # 退出循环
    # if not msg:
    #     break
    # 接收消息
    data,addr = udp_socket.recvfrom(1024)
    print("从服务端收到:",data.decode())

udp_socket.close()

