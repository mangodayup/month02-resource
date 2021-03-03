"""
基于多线程的并发模型　
重点代码
"""
from socket import *
from threading import Thread


# 　处理具体客户端请求
class Handle:
    def __init__(self, connfd):
        self.connfd = connfd

    def request(self):
        while True:
            data = self.connfd.recv(1024)
            if not data:
                break
            print(data.decode())
            self.connfd.send(b"OK")


# 线程类
class ThreadServer(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        self.handle = Handle(connfd)
        super().__init__(daemon=True)

    def run(self):
        self.handle.request()
        self.connfd.close()


# tcp模型
class TcpServer:
    """
    ｔｃｐ　套接字创建
    """
    def __init__(self, host="", port=0):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.sock = self._create_socket()

    def _create_socket(self):
        sock = socket()
        sock.bind(self.address)
        return sock

    # 启动函数
    def serve_forever(self):
        self.sock.listen(5)
        print("Listen the port %d" % self.port)
        while True:
            connfd, addr = self.sock.accept()
            print("Connect from", addr)
            # 为客户端创建线程
            t = ThreadServer(connfd)
            t.start()


if __name__ == '__main__':
    server = TcpServer(host="0.0.0.0", port=8888)
    server.serve_forever()
