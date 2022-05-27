#非阻塞式进程池
#非阻塞进程池，在满了了情况下需要等待出现空缺位置再填补进去，回调函数是等待任务完成之后才调用的
from multiprocessing import Pool#创建进程池
import time
import os
from random import random


def task(task_name):#task name 任务名
    print(task_name)
    start = time.time()#得到时间戳
    time.sleep(random()*2)
    end = time.time()
    return '开始做任务拉',task_name,'任务完成用时',(end-start),'进程id',os.getpid()

continer = []
#这里的n接收的是task()中的返回值
#callback_func回调函数
#回调函数是等待任务完成之后才调用的
def callback_func(n):
    continer.append(n)

if __name__ == '__main__':
    pool = Pool(5)#创建池子，5代表五个进程
    tasks = ['听音乐', '吃饭', '跑步', '打痘痘', '拉屎', '睡觉', '放屁']
    for task1 in tasks:
        pool.apply_async(task,args=(task1,),callback=callback_func)
#callback 回调函数，这儿接受的是回调函数的名字
#apply_async这个就是使用非阻塞式的，这个函数代表的意思是我现在使用的是非阻塞式池子
#第一个参数是函数名，第二个参数是传给函数的参数
#只要用进程池那么要挡住主进程不要让他结束，pool与主进程同生共死
    pool.close()##关闭进程池，不再接受新的进程
    pool.join()#让主进程堵住,把最后主进程要执行的 print('over!!!!!!') 挡住  让主进程让步  主进程阻塞等待子进程的退出
    for tsx in continer:
        print(tsx)
    print('over!!!!!!')
