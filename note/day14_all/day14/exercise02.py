"""
练习02：
创建2个分支线程
一个分支线程 打印 1--52 这些写数字
另一个分支线程 打印 A--Z 这些字母

要求在终端打印出的顺序为:12A34B...5152Z
"""
from threading import Thread,Lock

lock1 = Lock()
lock2 = Lock()

def print_num():
    for i in range(1,53,2):
        lock1.acquire()
        print(i)
        print(i + 1)
        lock2.release() # 给下面解锁

def print_chr():
    for i in range(65,91):
        lock2.acquire()
        print(chr(i))
        lock1.release() # 给上面解锁

t1 = Thread(target=print_num)
t2 = Thread(target=print_chr)

lock2.acquire() # 先把字母部分锁住

t1.start()
t2.start()


