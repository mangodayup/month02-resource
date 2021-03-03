"""
文件服务器 客户端代码
"""
import sys
from socket import *
from time import sleep


# 与服务端交互发起请求
class Handle:
    def __init__(self):
        self.server_addr = ("127.0.0.1", 8888)
        self.sock = self._connect_server()

    # 链接服务端
    def _connect_server(self):
        sock = socket()
        sock.connect(self.server_addr)
        return sock

    def do_list(self):
        self.sock.send(b"LIST")  # 发送请求
        response = self.sock.recv(128)  # 等待响应
        # 根据响应进行处理
        if response == b'OK':
            # 接收文件列表 file1\nfile2...
            files = self.sock.recv(1024 * 1024)
            print(files.decode())
        else:
            print("获取文件列表失败")

    def do_put(self, filename):
        try:
            file = open(filename, 'rb')
        except:
            print("要上传的文件不存在")
            return
        filename = filename.split('/')[-1]  # 提取文件名
        msg = "STOR " + filename
        self.sock.send(msg.encode())  # 发请求
        response = self.sock.recv(128)  # 等待响应
        # 分情况处理
        if response == b"OK":
            while True:
                data = file.read(1024)
                if not data:
                    break
                self.sock.send(data)
            file.close()
            sleep(0.1)
            self.sock.send(b"##")
        elif response == b"EXISTS":
            print("该文件已经存在")
        else:
            print("上传失败")

    def do_get(self, filename):
        msg = "RETR " + filename
        self.sock.send(msg.encode())  # 发请求
        response = self.sock.recv(128)  # 等待响应
        # 分情况处理
        if response == b"OK":
            file = open(filename, 'wb')
            # 接收文件，写入本地
            while True:
                data = self.sock.recv(1024)
                if data == b'##':
                    break
                file.write(data)
            file.close()
        elif response == b"NULL":
            print("该文件不存在")
        else:
            print("下载失败")

    def do_exit(self):
        self.sock.send(b"EXIT")
        self.sock.close()
        sys.exit("谢谢使用")


# 与用户交互
class FTPView:
    def __init__(self):
        self._handle = Handle()

    # 菜单函数
    def __display_menu(self):
        print()
        print("1.查看文件")
        print("2.上传文件")
        print("3.下载文件")
        print("4.退出服务")
        print()

    # 选择函数
    def __select_menu(self):
        item = input("请输入选项:")
        if item == '1':
            self._handle.do_list()
        elif item == '2':
            filename = input("输入要上传的文件:")
            self._handle.do_put(filename)
        elif item == '3':
            filename = input("输入要下载的文件:")
            self._handle.do_get(filename)
        elif item == '4':
            self._handle.do_exit()
        else:
            print("请输入正确选项")

    def start(self):
        while True:
            self.__display_menu()
            self.__select_menu()


if __name__ == '__main__':
    ftp = FTPView()
    ftp.start()
