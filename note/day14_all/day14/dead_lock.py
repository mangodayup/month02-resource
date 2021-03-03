"""
模拟死锁产生
"""
from threading import Thread,Lock
from time import sleep

# 账户类
class Account:
    def __init__(self,id,balance,lock):
        self._id = id
        self._balance = balance
        self.lock = lock

    #　取钱
    def withdraw(self,amount):
        self._balance -= amount

    #　存钱
    def deposit(self,amount):
        self._balance += amount

    def get_balance(self):
        return self._balance


#　转账方法
def transfer(from_,to,amount):
    from_.lock.acquire() # 锁住from
    from_.withdraw(amount) # 钱减少
    from_.lock.release() #　不会死锁

    sleep(0.1) # 延迟
    to.lock.acquire()  # 锁住to
    to.deposit(amount) # 钱增加

    # from_.lock.release() # 会产生死锁
    to.lock.release()




if __name__ == '__main__':
    tom = Account("tom", 5000, Lock())
    abby = Account("abby", 8000, Lock())

    t1 = Thread(target=transfer,args=(tom,abby,1000))
    t2 = Thread(target=transfer,args=(abby,tom,1000))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Tom:",tom.get_balance())
    print("Abby:",abby.get_balance())
