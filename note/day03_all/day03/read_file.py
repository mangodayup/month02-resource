"""
文件读取方法 演示
"""
# 读方式打开
# file = open("file.txt",'r')

# 二进制打开 读取出字节串
file = open("file.txt",'rb')

# 读取内容
data = file.read()
print(data)

# 循环读取文件内容
# while True:
#     data = file.read(1)
#     # 读取到文件最后继续会读到空字串
#     if data == "":
#         break
#     print(data,end="")

# 按行读取
# data = file.readline(1)
# print(data)
# data = file.readline()
# print(data)

# 读取所有行 返回列表
# lines = file.readlines(6)
# print(lines)

# 迭代每次获取一行
# for line in file:
#     print(line)

file.close()

