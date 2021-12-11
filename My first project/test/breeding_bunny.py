#!/usr/bin/python3
import threading
import logging

import time
logging.basicConfig(
    level=logging.INFO,
    format='(%(threadName)-10s) %(message)s',
)
count = 1                        ###兔子初始数量
month = 1
lock = threading.Lock()
# con = threading.Condition()
event = threading.Event()
class rabbit():                  ###rabbit对象，一对兔子
    def __init__(self,age=1) -> None:
        self.age = age

class breading(threading.Thread):
    def __init__(self,name,rabbit,Mon_max):
        super().__init__()
        self.rabbit = rabbit
        self.Mon_max = Mon_max
        self.name = name
        # self.event = event
    def run(self):
        global month
        global count
        global event
        while True:
            if self.rabbit.age >= 3:
                lock.acquire()
                count += 1
                lock.release()
                rab = rabbit()
                t = breading('第{}对兔子'.format(count),rab,self.Mon_max)
                t.start()
            if month >= self.Mon_max:
                break
            # con.acquire()
            # con.wait()
            event.wait()
            self.rabbit.age += 1
            event.clear()
            # con.release()   
class IncreaseMon(threading.Thread):
    def __init__(self,name,Mon_max=1) -> None:
        super().__init__()
        # self.month = month
        self.Mon_max = Mon_max
        self.name = name
    def run(self):
        global month
        # rab = rabbit()
        # bread = breading(rab,self.Mon_max)
        # bread.start()
        while  month <= self.Mon_max:
            # con.acquire()
            logging.info("时间过去了一个月......")
            logging.info("{}月兔子对数为{}".format(month,count))
            # logging.info("当前线程数为：{}".format(len(list(threading.enumerate()))))
            month += 1 
            event.set()
            time.sleep(3)
            # con.notify_all()
            # con.release()
if __name__=="__main__":
    Mon_max = int(input("输入持续生兔子的月份数目："))
    rab = rabbit()
    c = breading('第{}对兔子'.format(count),rab,Mon_max)
    c.start()
    a = IncreaseMon('IncreaseMon',Mon_max)
    a.start()
