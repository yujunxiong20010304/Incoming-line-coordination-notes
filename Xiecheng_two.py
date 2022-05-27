#greenlet  完成协程多任务  人工切换

from time import sleep

from greenlet import greenlet


def a():#任务A
    for i in range(5):
        print('A'+str(i))
        gb.switch()#切换
        sleep(0.1)

def b():#任务B
    for i in range(5):
        print('B'+str(i))
        gc.switch()#切换
        sleep(0.1)

def c():#任务B
    for i in range(5):
        print('C'+str(i))
        ga.switch()#切换
        sleep(0.1)

if __name__ == '__main__':
    ga = greenlet(a)
    gb = greenlet(b)
    gc = greenlet(c)

    ga.switch()
    gb.switch()
    gc.switch()
