"""
文件读写缓冲区
"""

# file = open("file.txt",'w')

# 设置为行缓冲
# file = open("file.txt",'w',buffering=1)

# 设置缓冲区大小
file = open("file.txt",'wb',buffering=10)

while True:
    data = input(">>")
    if not data:
        break
    file.write(data.encode())
    # file.flush() # 主动刷新缓冲

file.close()
