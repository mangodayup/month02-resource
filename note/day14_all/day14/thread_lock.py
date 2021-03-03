"""
线程同步互斥 2
"""
from threading import Thread , Lock

lock = Lock() # 锁对象

a = b = 0  # 共享资源

def value():
    while True:
        lock.acquire() # 上锁
        if a != b:
            print("a = %d,b = %d"%(a,b))
        lock.release() # 解锁

t = Thread(target=value)
t.start()

while True:
    lock.acquire()
    a += 1
    b += 1
    lock.release()