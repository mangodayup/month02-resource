from threading import Thread
from time import time


class Prime(Thread):
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
    # 一个线程
    # t = Prime(1, 100001)
    # t.start()
    # t.join() # 确保分支线程执行完

    # ４个线程
    jobs = []
    for i in range(1,100001,10000):
        t = Prime(i,i+10000)
        jobs.append(t)
        t.start()
    [i.join() for i in jobs]
    print("用时：",time()-begin)

# 一个线程 用时： 13.399898290634155
# 4个线程 用时： 13.258663177490234
# 10个线程 用时： 13.309852600097656
