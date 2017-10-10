import time
from multiprocessing.managers import  BaseManager
class Queuemanager(BaseManager):
    pass
print ('connect to server')
Queuemanager.register('get_task_queue')
Queuemanager.register('get_result_queue')
m = Queuemanager(address=('127.0.0.1',8001),authkey='qiye')
m.connect()
task = m.get_task_queue()
result = m.get_result_queue()
while (not task.empty()):
    image_url = task.get(True,timeout =5)
    print('run task download %s '%image_url)
    time.sleep(1)
    result.put('%s---success'%image_url)
    print('worker exit')

