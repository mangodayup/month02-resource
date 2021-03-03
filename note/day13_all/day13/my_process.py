"""
自定义一个进程类
"""
from multiprocessing import Process
from time import sleep

# 继承 Process类
class MyProcess(Process):
    def __init__(self,number):
        self.number = number
        super().__init__() # 加载父类实例变量

    # 重写父类方法--》进程任务
    def run(self):
        for i in range(self.number):
            sleep(2)
            print("run方法作为进程内容")

# 实例化进程对象
process = MyProcess(3)
process.start() # 启动进程运行run


######## 猜想 父类做法 ########
# class Process:
#     def __init__(self,target=None):
#         self._target = target
#
#     def run(self):
#         if self._target:
#             self._target()
#
#     def start(self):
#         #　创建进程
#         # 进程加载　
#         self.run()







