"""
IO多路复用 示例 epoll
"""
from select import *
from socket import *

# 准备几个IO对象
tcp_socket = socket()
tcp_socket.bind(("0.0.0.0",8888))
tcp_socket.listen(5)

udp_socket = socket(AF_INET,SOCK_DGRAM)

ep = epoll() # 生成epoll对象

# 查找字典 始终跟关注的IO保持一致
map = {
    tcp_socket.fileno():tcp_socket,
    udp_socket.fileno():udp_socket
}
ep.register(tcp_socket,EPOLLIN) # 关注IO
ep.register(udp_socket,EPOLLIN|EPOLLOUT) # 关注IO

print("开始监控IO发生")
events = ep.poll()
print("events:",events) # [(fileno,event),...]

# map[fileno].accept()

# ep.unregister(fileno)



