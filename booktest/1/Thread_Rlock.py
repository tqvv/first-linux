#coding:utf-8
import threading
#Rlock有问题？
mylock = threading.Rlock()
num=0
class myThread(threading.Thread):
    def __int__(self,name):
        threading.Thread.__init__(self,name=name)
    def run(self):
        global num
        while True:
            mylock.acquire()
            print '%slocked,Number:%d'%(threading.current_thread().name,num)
            if num >=4:
                mylock.release()
                print'%s released,number:%d'%(threading.current_thread().name,num)
                break
            num+=1
            print'%s released,number:%d'%(threading.current_thread().name,num)
            mylock.release()
if __name__ == '__main__':
    thread1 = myThread('Thread1')
    thread2 = myThread('Thread2')
    thread1.start()
    thread2.start()
