#线程two
#线程可以共享全局变量
from threading import Thread

money = 1000


def run1():
    global money
    for i in range(100):
        money -= 1


def run2():
    global money
    for i in range(100):
        money -= 1


if __name__ == '__main__':
    th1 = Thread(target=run1,name='th1')
    th2 = Thread(target=run2, name='th2')


    #启动
    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(money)
