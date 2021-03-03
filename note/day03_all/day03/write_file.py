"""
文件写入操作示例
"""
# 写方式打开文件
# file = open("file.txt","w")

# 二进制
# file = open("file.txt","wb")

# 追加方式打开
file = open("file.txt","ab")


# 写入内容
n = file.write("hello 死鬼\n".encode())
file.write("哎呀，干啥\n".encode())
print("写入 %d 字节"%n)

# 将列表数据写入文件
# data = [
#     "接着奏乐\n",
#     "接着舞\n"
# ]
#
# file.writelines(data)

file.close()

