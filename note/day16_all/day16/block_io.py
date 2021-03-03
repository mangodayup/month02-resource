"""
非阻塞IO演示
"""
from socket import *
from time import ctime,sleep

# 打开一个日志文件
file = open("my.log",'a')

# 创建tcp套接字
sock = socket()
sock.bind(("0.0.0.0",8888))
sock.listen(5)

# 将套接字设置非阻塞
# sock.setblocking(False)

# 设置超时时间
sock.settimeout(2)

# 循环连接客户端
while True:
    try:
        connfd,addr = sock.accept()
        print("Connect from",addr)
    except (BlockingIOError,timeout) as e:
        # 模拟一个与accept无关的事情
        msg = "%s : %s\n"%(ctime(),e)
        file.write(msg)
        sleep(2)
    else:
        data = connfd.recv(1024)
        print(data.decode())

