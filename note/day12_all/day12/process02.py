"""
含有参数的进程函数
进程结束控制
"""
from multiprocessing import Process
from time import sleep


# 带有参数的进程函数
def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" % name)
        print("I'm working...")


# 按照位置传参
# process = Process(target=worker,
#                   args=(2, "Tom"))

# 按照关键字传参
# daemon=True子进程随父进程退出
process = Process(target=worker,
                  args=(2,),
                  kwargs={"name":"Tom"},
                  daemon=True)
process.start()

# 父进程等待子进程退出
# process.join()
sleep(3)
print("=======================")