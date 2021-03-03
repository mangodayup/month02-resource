"""
os模块文件处理
"""
import os

print("文件大小：",os.path.getsize("file.txt"))
print("文件列表：",os.listdir("."))
print("文件是否存在：",os.path.exists("my.log"))
os.remove("file.txt") # 删除文件