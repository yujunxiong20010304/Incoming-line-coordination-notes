#线程同步的概念
#线程同步（锁）会延长运行时间
#python底层只要用线程就会默认加锁，所以之前的Multithereading运行结果没有出问题，但是只要运算率达到一定程度就会自动释放这个锁
#
'''
GIL全局解释器锁（python自带的坑）
n-=1 ————》n=n-1
线程在任何时候都可能被抢夺执行权，可能n-1做了，但还没来的及赋值就被抢夺了执行权
'''
from threading import Thread

n = 0
def task1():
    global n
    for i in range(100000000):
        n += 1
    print('task1中的值是：',n)

def task2():
    global n
    for i in range(100000000):
        n += 1
    print('task2中的值是：',n)


if __name__ == '__main__':
    th1 = Thread(target=task1,name=task1)
    th2 = Thread(target=task2, name=task2)

    th1.start()
    th2.start()

    th1.join()
    th2.join()
    print('最后n的值',n)
