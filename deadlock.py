#死锁
'''
在开发过程中使用线程，在线程间共享多个资源的时候，如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁，
尽管死锁很少发生，但一旦发生就会造成应用的停止响应，程序不会做任何事情
'''

#避免死锁
#1。重构代码
#给lock.acquire(timeout = )加个超时
from threading import Thread,Lock
import time

lockA = Lock()
lockB = Lock()
#自定义线程
#无论是进程还是线程，重写的方法都是run()方法
class MyThread(Thread):
    def run(self):#调用start就会自动启动run()
        if lockA.acquire():#如果可以获取锁则返回True
            print(self.name+'获取了A锁')
            time.sleep(0.5)
            if lockB.acquire():
                print(self.name+'又获取了B锁，原来还有A锁')
                lockB.release()
            lockA.release()


class MyThread1(Thread):
    def run(self):#调用start就会自动启动run()
        if lockB.acquire():#如果可以获取锁则返回True
            print(self.name+'获取了B锁')
            time.sleep(0.5)
            if lockA.acquire():
                print(self.name+'又获取了A锁，原来还有B锁')
                lockA.release()
            lockB.release()

if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread1()

    t1.start()
    t2.start()
