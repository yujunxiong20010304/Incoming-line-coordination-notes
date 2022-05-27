#进程间的通信  如何使用(模拟下载过程)
from multiprocessing import Process,Queue
from time import sleep
import os

def download(q):#这个函数用来下载
    images = ['gril.jpg','boy.jpg','man.jpg']
    for image in images:
        print('正在下载',image)
        sleep(0.5)
        q.put(image)

#（1）
'''def getfile(q):#这个函数用来保存东西
    while q.empty():
        file = q.get()
        print('{}什么文件保存成功'.format(file))'''
#（2）
'''
if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download,args=(q,))
    p2 = Process(target=getfile,args=(q,))
    p1.start()
    p2.start()
'''

#（3）
def getfile(q):#这个函数用来保存东西
    while True:
        try:
            file = q.get(timeout=5)
            print('{}什么文件保存成功'.format(file))
        except:
            print('没有了')
#（4）
if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download,args=(q,))
    p2 = Process(target=getfile,args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()

#自我总结：如果在这个程序中最后是（1）和（4）进行搭配，那么最后的结果是   正在下载 gril.jpg正在下载 boy.jpg正在下载 man.jpg
#原因是q.empty为假，为什么为假呢？因为加了p1.join()那么在p1这个进程不执行完的化q这个队列中是没有值的
#而（3）（4）搭配join()的原因是等待p1执行完全后在通过队列传值过去
#join()可以理解为插队，因为进程用它之后，那么就要等这个进程执行完后才能执行下一个进程
