"""
练习02：
从父进程中不断录入学生成绩，包括姓名和分数
，在子进程中判断这个学生的成绩是否大于等90，
如果是则将其保存起来
保存为一个字典
student = {name:score}

自己设定父子进程结束方式，结束时打印字典
内容
"""
from multiprocessing import Process, Queue
import sys

# 消息队列 存储仓库
q = Queue()


# 数据筛选 子进程
def select_student():
    student = {}
    while True:
        name, score = q.get()  # 得到元组
        if name == 'exit':
            print(student)
            sys.exit()  # 收到特殊标志退出
        elif score >= 90:
            student[name] = score  # 添加到字典


def input_info():
    while True:
        name = input("Name:")
        if not name:
            q.put(("exit", 0))
            break
        score = int(input("Score:"))
        q.put((name, score))  # 放入消息队列


p = Process(target=select_student)
p.start()
input_info()
