#自定义进程
from multiprocessing import Process#导入Process这个类
class myProcess(Process):#继承这个类
    def __init__(self,name,x):
        super(myProcess,self).__init__(target=x) #p1 = Process(target=text1, name='进程1')把x类似这样传递
        self.name = name
    def run(self):
        while True:
            print('进程的名字是：{}'.format(self.name))
            super().run()#调用父类的run()方法
def t():
    print('ttttttttttttttt')

def o():
    print('oooooooooooooooo')
p = myProcess('小王',t)
p.start()
p2 = myProcess('小O',o)
p2.start()
#虽然这个程序调用了父类的run()方法，但是子类调用的是父类的start()方法
