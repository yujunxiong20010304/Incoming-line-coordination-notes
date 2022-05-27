#多线程基础讲解
#线程的效果类似与进程，但之所以有线程，是为了减少开销
#线程并发执行
import threading#线程模块
from time import sleep
from threading import Thread

def download(q):#这个函数用来下载
    images = ['gril.jpg','boy.jpg','man.jpg']
    for image in images:
        print('正在下载',image)
        sleep(q)
        print('{}下载成功'.format(image))

def listenmusic():
    musics = ['量子老虎','什么是快乐星球','昨夜的你','家有女友']
    for music in musics:
        sleep(0.5)
        print('正在听{}'.format(music))

if __name__ == '__main__':
    # 创建线程对象
    t = Thread(target=download, name='下载', args=(1,))
    t.start()
    t1 = Thread(target=listenmusic,name='听歌')
    t1.start()

