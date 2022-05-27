#阻塞式进程池
import os
import time
from multiprocessing import Pool
from random import random


def task(task_name):#task name 任务名
    start = time.time()#得到时间戳
    print(task_name)
    time.sleep(random()*2)
    end = time.time()
    print('开始做任务拉',task_name,'任务完成用时',(end-start),'进程id',os.getpid())


if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['听音乐', '吃饭', '跑步', '打痘痘', '拉屎', '睡觉', '放屁']
    for task1 in tasks:
        pool.apply(task, args=(task1,))#不需要回调

    print('over!!!')
