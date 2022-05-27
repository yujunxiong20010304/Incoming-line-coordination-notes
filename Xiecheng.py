#协程（微线程）
#生成器完成协程
#协程：耗时操作时使用（网络请求，网络下载（爬虫），io操作（文件读写））
#利用成器：yield
from time import sleep
def task1():
    for i in range(3):
        print('A'+str(i))
        yield
        sleep(0.2)

def task2():
    for i in range(3):
        print('B'+str(i))
        yield
        sleep(0.2)

if __name__ == '__main__':
    g1 = task1()
    g2 = task2()

    while True:
        try:
            next(g1)#next 返回迭代器的下一个项目
            next(g2)
        except:
            break


