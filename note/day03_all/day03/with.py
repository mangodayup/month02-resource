"""
with 操作
"""
# 打开文件
with open("file.txt") as file:
    data = file.read()
    print(data)

# with语句块结束 file会自动销毁
