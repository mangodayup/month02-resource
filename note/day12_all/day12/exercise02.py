"""
练习02：
创建一个子进程，子进程传入两个整数
求这两个整数之间的所有质数之和

1   1000 ---》打印出 1--1000的质数之和

质数 ： 只能被1 和它本身整除
       >1 的整数
"""
from multiprocessing import Process

# 判断一个数是否为质数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n // 2 + 1):
        if n % i == 0:
            return False
    return True

# 求和
def prime(min,max):
    result = []
    for i in range(min,max):
        if is_prime(i):
            result.append(i)
    print(sum(result))

p = Process(target=prime,args=(1,1000))
p.start()








