"""
IO多路复用 示例 select
"""
from select import select
from socket import *

# 准备几个IO对象
tcp_socket = socket()
tcp_socket.bind(("0.0.0.0",8888))
tcp_socket.listen(5)

udp_socket = socket(AF_INET,SOCK_DGRAM)

file = open("my.log")

print("开始监控IO发生")
rs,ws,xs = select([tcp_socket,file],[udp_socket],[])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)




