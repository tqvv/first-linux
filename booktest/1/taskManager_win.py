import random,time,Queue
from multiprocessing.managers import  BaseManager
from multiprocessing import  freeze_support
task_number = 10
task_queue = Queue.Queue(task_number);
result_queue = Queue.Queue(task_number);
def get_task():
    return task_queue
def get_result():
    return result_queue
class Queuemanager(BaseManager):
    pass
def win_run():
    Queuemanager.register('get_task_queue',callable=get_task())
    Queuemanager.register('get_result_queue',callable=get_result())
    manager = Queuemanager(address=('127.0.0.1',8001),authkey='qiye')
    manager.start()
    try:
        task = manager.get_task_queue()
        result = manager.get_result_queue()
        for url  in ["ImageUrl_" + str(i) for i in range(10)]:
            print 'put task %s......'%url
            task.put(url)
            print 'try get result....'
        for i in range(10):
            print 'result is %s'%result.get(timeout=10)
    except:
        print('Manager error')
    finally:
        manager.shutdown()
if __name__ =='__main__':
    #freezs_support()
    win_run()


