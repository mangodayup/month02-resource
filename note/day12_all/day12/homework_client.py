from socket import *

# 服务器地址
server_address = ("127.0.0.1",8888)

def chat(msg):
    tcp_socket = socket()
    tcp_socket.connect(server_address)
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024).decode()
    tcp_socket.close()
    return data # 服务端回复

def main():
    while True:
        msg = input("我：")
        if not msg:
            break
        result = chat(msg)
        print("小美：",result)

if __name__ == '__main__':
    main()




