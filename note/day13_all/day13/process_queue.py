"""
进程间通信　：　消息队列
"""
from multiprocessing import Process,Queue

#　创建消息队列
q = Queue(5)

#　进程函数
def handle(num):
    result = 0
    for i in range(num + 1):
        result += i
    # 将结果存入消息队列
    q.put(result)


p = Process(target=handle,args=(20,))
p.start()

result = q.get() # 从消息队列获取到子进程结果

# 父进程需要子进程的结果做下一步工作
if result > 5000:
    print("喔喔喔，今年收成可以")
else:
    print("哎哎哎，明年继续努力")





