#生产者和消费者（也就是两个线程间的通信）
import threading
import queue
import random
import time

def produce(q):
    i = 0
    while i<10:
        num = random.randint(1,100)
        q.put('生产者产生数据：%d' % num)
        print('生产者产生数据：%d' % num)
        time.sleep(1)
        i += 1
    q.put(None)
    #完成任务
    q.task_done()#主要是给join用的，每次get后需要调用task_done，直到所有任务都task_done。join才取消阻塞


def consume(q):
    while True:
        item = q.get()
        if item == None:#is用于判断两个变量引用变量是否为同一个  ==引用变量的值是否相等
            break
        print('消费者获取到%s' % item)
        time.sleep(4)
    #完成任务
    q.task_done()


if __name__ == '__main__':
    q = queue.Queue(1000000000)
    arr = []

    #创建生产者
    th = threading.Thread(target=produce,args=(q,))
    th.start()

    #创建消费者
    tc = threading.Thread(target=consume,args=(q,))
    tc.start()
    th.join()
    tc.join()
