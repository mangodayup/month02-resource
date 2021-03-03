"""
文件打开方法 演示
"""

# 读方式打开文件
# file = open("../3.txt",'r')
# print(file)

# 写方式打开文件 清空file.txt
# file = open("file.txt",'w')
# print(file)

# 追加方式打开 不清空file.txt
file = open("file.txt",'a')
print(file)

# 销毁文件对象
file.close()