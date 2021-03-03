"""
创建多个子进程示例
"""
from multiprocessing import Process
from time import sleep
import os,sys

def th1():
    sleep(4)
    print("吃饭")
    print(os.getppid(),"--",os.getpid())

def th2():
    sleep(2)
    sys.exit("不睡觉喽") # 进程退出
    print("睡觉")
    print(os.getppid(),"--",os.getpid())

def th3():
    sleep(3)
    print("打豆豆")
    print(os.getppid(),"--",os.getpid())


# 遍历每个函数，创建对应进程
jobs = [] # 存储进程兑对象
for th in [th1,th2,th3]:
    p = Process(target=th)
    jobs.append(p) # 存入列表
    p.start()

############### 另一种写法  ###########
# def th(sec,thing):
#     sleep(sec)
#     print(thing)
#     print(os.getppid(),"--",os.getpid())
#
# # 遍历每个函数，创建对应进程
# jobs = [] # 存储进程兑对象
# for i in [(4,"吃饭"),(2,"睡觉"),(3,'打豆豆')]:
#     p = Process(target=th,args=i)
#     jobs.append(p) # 存入列表
#     p.start()

for i in jobs:
    i.join()
print("子进程都结束了")
