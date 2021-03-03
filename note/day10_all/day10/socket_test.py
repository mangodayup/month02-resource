"""
socket_test.py
套接字 函数使用示例
"""
import socket

# 创建udp套接字
udp_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM)

# 绑定地址
# 1.网络地址 别人可以通过该ip地址与我通信
# udp_socket.bind(("172.40.91.124",8888))

# 2.测试地址 别人可以通过127.0.0.1地址与我
# 通信，但是对方程序需要和我在同一计算机上
# udp_socket.bind(("127.0.0.1",8888))

# 3.万能地址 别人可以通过以上两种情形访问
udp_socket.bind(("0.0.0.0",8888))






