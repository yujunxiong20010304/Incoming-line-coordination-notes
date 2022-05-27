#进程间通信  基础知识点
#put()如果queue满了则只能等待，除非有'空地'则添加成功，只要取一下就空出来了
from multiprocessing import Queue#用于进程间的通信
q = Queue(5)#往队列中塞东西最多只能塞5个
q.put('A')#put()向队列中放东西
q.put('B')
q.put('C')
q.put('D')
q.put('E')
#print(q.qsize())#打印队列长度，但在mac os上不能使用
if q.full():#判断队列是否满了，返回一个真假    q.empty()判断队列是否是空的
    print('队列以满')
else:
    q.put('F',timeout=3)#timeout在这儿等待三秒钟，如果还没有空位置就报异常


#get()获取队列中的值
print(q.get(timeout=2))#timeout在这儿等待2秒钟，如果还取不出就报异常
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get())
print(q.get())

#q.put_nowait()
#q.get_nowait() 不阻塞,取完之后没取的就报异常

