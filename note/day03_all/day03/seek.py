"""
文件偏移量
"""
# 可读可写
file = open("file.txt",'w+')

file.write("你好世界")
file.flush()

print("当前位置:",file.tell())
# 将文件偏移量重置到开头
file.seek(3,0)

# file.write("ABC")

data = file.read()
print(data)

file.close()
