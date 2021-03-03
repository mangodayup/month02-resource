"""
练习03：
编写一个程序，完成简单的日志（my.log）写入
执行程序时，循环写入如下格式内容
每2秒写入一行，每行实时存入到文件中

1. 2020-1-1  10:10:10
2. 2020-1-1  10:10:12
3. 2020-1-1  10:10:14

import time
localtime()
sleep()
"""
from time import *

# 打开文件
file = open("my.log",'a+',buffering=1)

file.seek(0,0) # 文件偏移在开头
n = 1 # 序号
for line in file:
    n += 1

while True:
    tm = "%d-%d-%d %d:%d:%d"%localtime()[:6]
    file.write("%d. "%n+tm+'\n')
    n += 1
    sleep(2)