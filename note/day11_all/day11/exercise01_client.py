from socket import *

filename = "./jialing.jpg"

def send_file(sock):
    file = open(filename,'rb')
    # 边读取，边发送
    while True:
        data = file.read(1024)
        if not data:
            break
        sock.send(data)
    file.close()

def main():
    tcp_socket = socket()
    tcp_socket.connect(("172.40.91.124",8888))
    # 发送文件
    send_file(tcp_socket)
    tcp_socket.close()

if __name__ == '__main__':
    main()