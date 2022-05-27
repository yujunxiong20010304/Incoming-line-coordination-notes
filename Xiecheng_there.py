#gevent 自动切换协程
import gevent
import time
from gevent import monkey#猴子补丁
monkey.patch_all()#打补丁,之所以要用这个是因为在gevent中有了sleep，猴子补丁在地层偷偷把time.sleep替换了
def a():#任务A
    for i in range(5):
        print('A'+str(i))
        time.sleep(0.1)

def b():#任务B
    for i in range(5):
        print('B'+str(i))
        time.sleep(0.1)

def c():#任务B
    for i in range(5):
        print('C'+str(i))
        time.sleep(0.1)

if __name__ == '__main__':
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)

    g1.join()
    g2.join()
    g3.join()
