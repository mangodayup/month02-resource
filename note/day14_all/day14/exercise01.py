"""
练习01：
现在有500张票  记为 T1 -- T500

现有10个窗口  记为 W1 -- W10  同时售票
直到所有票卖完为止

使用10个线程模拟窗口卖票过程，每卖出一张
打印：  W1 -- T236
每张票出票时间 为 0.1s
"""
from threading import Thread
from time import sleep

# 准备500张票
tickets = ["T%d" % i for i in range(1, 501)]

# 卖票函数
def sell(w):
    # tickets 不为空则执行循环
    while tickets:
        print("%s -- %s"%(w,tickets.pop(0)))
        sleep(0.1)  # 间隔


# 10个线程表示10个窗口
for i in range(1,11):
    t = Thread(target=sell,args=("W%d"%i,))
    t.start()