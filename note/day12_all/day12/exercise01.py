"""
练习01：
编写一个程序，将一个大文件分割为2部分
，上下半部分各自分出一个新文件
要求上下两个部分同时查分出来，拆分完成后
请求打印提示  “已拆分完毕”

注意： 文件按照字节数划分上下部分
      os.path.getsize()
      file.seek() # 文件偏移量
"""
from multiprocessing import Process
import os

filename = "./zly.jpg"
size = os.path.getsize(filename)

# 如果父进程打开文件，子进程直接用fr
# 那么父子进程使用同一个文件偏移量，会相互影响
# fr = open(filename,'rb')

# 复制上半部分
def top():
    fr = open(filename,'rb')
    fw = open('top.jpg','wb')
    n = size // 2 # 一半的字节数
    while n >= 1024:
        fw.write(fr.read(1024))
        n -= 1024
    else:
        fw.write(fr.read(n))
    fr.close()
    fw.close()

# 复制下半部分
def bot():
    fr = open(filename, 'rb')
    fw = open('bot.jpg', 'wb')
    fr.seek(size//2,0) # 将文件偏移量移动到中间
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

# 子进程执行一个
p = Process(target=top)
p.start()
# 父进程执行一个
bot()

p.join() # 等待子进程结束
print("文件拆分完毕")