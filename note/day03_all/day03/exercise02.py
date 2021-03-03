"""
练习02： 重点练习
编写一个函数，参数是一个指定的文件，调用函数
将该文件赋值到当前程序运行目录下
注意：要复制的文件类型不确定
     文件可能比较大，最好不要一次读取
思路：从源文件读取内容，写入新文件
"""

def copy_file(filename):
    new_file = filename.split('/')[-1]
    fr = open(filename,'rb') # 原文件
    fw = open(new_file,'wb') # 新文件
    # 边读边写
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()


copy_file("/home/tarena/nba.jpg")
