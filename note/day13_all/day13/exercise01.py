"""
使用自定义进程类完成，传入两个数值
求两个数值之间的质数之和
"""
from multiprocessing import Process
from time import time


class Prime(Process):
    def __init__(self, min, max):
        self.__min = min
        self.__max = max
        super().__init__()

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True

    def run(self):
        result = []
        for i in range(self.__min, self.__max):
            if self.is_prime(i):
                result.append(i)
        print(sum(result))


if __name__ == '__main__':
    begin = time()
    # 一个进程
    # p = Prime(1, 100001)
    # p.start()
    # p.join() # 确保子进程执行完

    # 20个进程
    jobs = []
    for i in range(1,100001,5000):
        p = Prime(i,i+5000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]  # 等4个进程结束
    print("用时：",time()-begin)

# 一个进程 用时： 13.441189289093018
# 4个进程 用时： 7.635168075561523
# 10个进程 用时： 6.701323747634888
# 20个进程 用时： 6.704560995101929