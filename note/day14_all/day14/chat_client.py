"""
群聊聊天室客户端
"""
from socket import *
from multiprocessing import Process

# 服务器地址
SERVER_ADDR = ("119.3.158.53", 8888)


# 进入聊天室
def login(sock):
    while True:
        name = input("请输入昵称:")
        # 按照协议发送请求
        msg = "LOGIN " + name
        sock.sendto(msg.encode(), SERVER_ADDR)
        # 接收结果
        result, addr = sock.recvfrom(128)
        if result == b"OK":
            print("您已进入聊天室")
            return name
        else:
            print("该昵称已存在")


# 子进程负责接收消息
def recv_msg(sock):
    while True:
        msg, addr = sock.recvfrom(1024 * 10)
        print("\n" + msg.decode() + "\n发言:", end="")


def send_msg(sock, name):
    while True:
        try:
            content = input("发言:")
        except:
            content = "exit"
        if not content:
            continue
        elif content == 'exit':
            msg = "EXIT " + name
            sock.sendto(msg.encode(), SERVER_ADDR)
            break
        msg = "CHAT %s %s" % (name, content)
        sock.sendto(msg.encode(), SERVER_ADDR)


# 入口函数
def main():
    # udp套接字客户端
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(("0.0.0.0", 55258))  # 防止地址变化

    # 进入聊天室
    name = login(sock)

    # 　聊天
    p = Process(target=recv_msg, args=(sock,), daemon=True)
    p.start()
    send_msg(sock, name)


if __name__ == '__main__':
    main()
