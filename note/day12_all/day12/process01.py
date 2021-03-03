"""
创建进程示例
1.将需要新进程执行的事件封装为函数
2.通过模块的Process类创建进程对象，关联函数
3.通过进程对象调用start启动进程
"""
import multiprocessing as mp
from time import sleep

# 全局变量
a = 1

# 编写进程函数
def fun():
    print("开始运行一个进程")
    sleep(2)
    global a
    print("a =",a)
    a = 10000 # 修改全局变量
    print("进程执行完毕喽...")

# 创建进程对象，绑定函数
process = mp.Process(target=fun)

# 启动进程 执行绑定的函数 进程诞生
process.start()

print("诶呦喂，我也执行点内容")
sleep(3)
print("诶呦，我也执行完了")

# 子进程执行完毕
print("a:",a) # 1





