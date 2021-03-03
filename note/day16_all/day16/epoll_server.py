"""
基于IO多路复用的网络并发模型 epoll
重点代码 ！！
"""
from socket import *
from select import *

HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 存储关注的IO对象 {fileno:object}
map = {}

# 处理客户端连接
def connect(ep,fd):
    connfd, addr = map[fd].accept()
    print("Connect from", addr)
    # 连接的客户端套接字加入到监控列表
    connfd.setblocking(False)
    ep.register(connfd,EPOLLIN|EPOLLET) # 设置边缘触发
    map[connfd.fileno()] = connfd # 维护字典


# 处理客户端消息
def handle(ep,fd):
    data = map[fd].recv(1024)
    if not data:
        ep.unregister(fd)  # 客户端断开移除关注
        map[fd].close()
        del map[fd]  # 从字典删除
        return
    print(data.decode())
    # map[fd].send(b"OK")
    ep.unregister(fd) # 先移除
    ep.register(fd,EPOLLOUT) # 关注写

# 程序入口函数
def main():
    # tcp套接字
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    print("Listen the port %d" % PORT)
    # IO多路复用多和非阻塞IO配合
    sock.setblocking(False)

    ep = epoll() # 创建epoll对象
    ep.register(sock,EPOLLIN) # 初始关注
    map[sock.fileno()] = sock
    # 循环监控IO发生，并处理发生的IO事件
    while True:
        events = ep.poll()
        print("你有新的IO需要处理哦",events)
        # events --> [(fileno,event)]
        for fd,event in events:
            if fd == sock.fileno():
                connect(ep,fd)  # 处理客户端连接
            # elif event == EPOLLIN:
            #     handle(ep,fd)  # 处理客户端发送消息
            # elif event == EPOLLOUT:
            #     map[fd].send(b"OK")
            #     ep.unregister(fd)
            #     ep.register(fd, EPOLLIN)


if __name__ == '__main__':
    main()
