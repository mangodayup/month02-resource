"""
练习04：
编写一个程序，删除主目录下FTP文件夹中
大小不到10K的所有文件（假设这个文件夹
中没有子文件夹）
"""
import os

dir = "/home/tarena/FTP/"

for file in os.listdir(dir):
    filename = dir + file # 拼接路径
    if os.path.getsize(filename) < 1024 * 10:
        os.remove(filename)
