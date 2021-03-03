#!/usr/bin/python3

result = 1 # 获取最后结果

for i in range(1,21):
    if i % 2 == 1:
        result *= i 

print("结果:",result)
