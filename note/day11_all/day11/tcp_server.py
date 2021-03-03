"""
tcp服务端 程序示例
重点代码 !!!
"""
from socket import *
from time import sleep

# 创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0",8888))

# 设置为监听套接字
tcp_socket.listen(5)

while True:
    # 等待处理客户端连接
    print("等待客户端连接......")
    connfd,addr = tcp_socket.accept()
    print("连接了:",addr)

    # 收发消息
    while True:
        data = connfd.recv(1024)
        # 客户端退出data为空字节串
        if not data or data == b'##':
            break
        print("收到:",data.decode())
        connfd.send(b"Thanks#")
        sleep(0.1) # 控制发送速度

    connfd.close()

# 关闭套接字
tcp_socket.close()






