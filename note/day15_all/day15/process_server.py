"""
基于多进程的网络并发模型
重点代码 ！！

创建网络套接字
等待客户端连接
有客户端连接，则创建新的进程具体处理请求
父进程继续等待连接其他客户端
如果客户端退出，则销毁对应的进程
"""
from socket import *
from multiprocessing import Process
import sys

# 服务器绑定地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 处理客户端具体请求　（根据业务逻辑编写）
def handle(connfd):
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b"OK")
    connfd.close()

# 并发网络服务搭建
def main():
    # 创建tcp套接字
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    print("Listen the port %d" % PORT)

    # 循环等待客户端连接
    while True:
        try:
            connfd,addr = sock.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            sock.close()
            sys.exit("服务端退出")

        # 为连接上的客户端创建子进程
        p = Process(target=handle,args=(connfd,),daemon=True)
        p.start()

if __name__ == '__main__':
    main()


