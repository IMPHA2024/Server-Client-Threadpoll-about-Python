'''
先同步
需要一个输入（抽象为func(args,kwargs)）
输入由一个伪class元组包装

输入放入queue中

work函数依次get 输入
work 内实现func(args,kwargs)
'''
import threading
import socket
import queue

class process:
    def __init__(self,num,top):
        self.task_queue = queue.Queue(maxsize= top)
        self.thread_pool = []
        self._finish = False
        for _ in range(num):
            t = threading.Thread(target=self._work)
            t.start()
            self.thread_pool.append(t)
    def input(self,func,*args,**kwargs):
        if self.task_queue.full():
            return
        #print("sss")
        #print(args)
        self.task_queue.put((func,args,kwargs))
    def _work(self):
        while not self._finish :
            try:
                #print("start trying")
                task = self.task_queue.get(timeout= 0.5)
                if task is None:
                    break
                
                func , args,kwargs = task
                
                func(*args,**kwargs)
                
                self.task_queue.task_done()
            except queue.Empty:
                #print("queue is empty")
                continue
    def shutdown(self,wait=True):
        self._finish = True
        if wait:
            self.task_queue.join()

def connect(server):
    try:
        client , addr = server.accept()
        client.send("connect".encode('utf-8'))
        print("connect")
        data = client.recv(1024)
        if data.decode('utf-8') == 'exit':
            print("close connent")
            running = False
        else:
            print(f"收到客户端 {addr} 的消息：{data.decode('utf-8')}")
            client.send(f"已收到你的消息：{data.decode('utf-8')}".encode('utf-8'))
        client.close()
    except BlockingIOError:
        print("no blocking")
        pass
    except Exception as e:
        print("error : {e}")

IP = '0.0.0.0'
PORT = 8888
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((IP , PORT))
server.listen(5)
print("listen")

running = True
s = process(5,5)
while running:
    s.input(connect,server)
server.close()
'''
def func(a,b):
    print(a+b)
def test():
    p = process(5,5)
    for i in range(1,6):
        p.input(func,i,i+1)        

test()'''