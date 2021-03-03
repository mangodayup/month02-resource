"""
创建线程示例 2
"""
from threading import Thread
from time import sleep

# 带有参数的线程函数
def func(sec,name):
    print("%s 线程开始执行"%name)
    sleep(sec)
    print("%s 线程执行完喽"%name)

# 循环创建线程
for i in range(5):
    t = Thread(target=func,args=(2,),
               kwargs={"name":"T-%d"%i},
               daemon=True)
    t.start()