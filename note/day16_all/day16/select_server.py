"""
基于IO多路复用的网络并发模型
重点代码 ！！
"""
from socket import *
from select import select

HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 存放要监控的IO对象
rlist = []
wlist = []
xlist = []


# 处理客户端连接
def connect(sock):
    connfd, addr = sock.accept()
    print("Connect from", addr)
    # 连接的客户端套接字加入到监控列表
    connfd.setblocking(False)
    rlist.append(connfd)


# 处理客户端消息
def handle(connfd):
    data = connfd.recv(1024)
    if not data:
        rlist.remove(connfd)  # 客户端断开移除关注
        connfd.close()
        return
    print(data.decode())
    # connfd.send(b"OK")
    wlist.append(connfd) # 加入写操作

# 程序入口函数
def main():
    # tcp套接字
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    print("Listen the port %d" % PORT)
    # IO多路复用多和非阻塞IO配合
    sock.setblocking(False)
    rlist.append(sock)
    # 循环监控IO发生，并处理发生的IO事件
    while True:
        rs, ws, xs = select(rlist, wlist, xlist)
        # 当rlist监控的IO增加，再就绪时要分情况讨论
        for r in rs:
            if r is sock:
                connect(r)  # 处理客户端连接
            else:
                handle(r)  # 处理客户端发送消息

        for w in ws:
            w.send(b"ok")
            wlist.remove(w) # 每次写完移除


if __name__ == '__main__':
    main()
