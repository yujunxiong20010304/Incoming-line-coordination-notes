#进程
from multiprocessing import Process
import time
lisy = []
i = 0
def text1():
    global i
    while True:
        i+=1
        time.sleep(3)
        print('_______1___________')
        lisy.append(i)
        print(1,lisy)
def text2():
    global i
    while True:
        time.sleep(1)
        print('_________2___________')
        i += 1
        lisy.append(i)
        print(2,lisy)
def text3():
    print('asdasdasda')
if __name__ == '__main__':#开子进程的代码必须写在这一行的下面
        p1 = Process(target=text1, name='进程1')
        p1.start()
        p2 = Process(target=text2,name='进程2')
        p2.start()

        print('-------------')
        text3()
