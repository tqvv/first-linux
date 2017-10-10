
from multiprocessing import Pool
import os, time, random
def run_task(name):
    print 'Task %s (pid = %s) is running......' %(name, os.getpid())
    time.sleep(random.random() * 3)
    print 'Task %s end.' %name
if __name__=='__main__':
    print 'Current process %s.' %os.getpid()
    p = Pool(processes=5)
    for i in range(5):
        #该句语法错误
        p.apply_async(run_task,args=(i,))
        print 'Waiting for all subprocesses done......'
        p.close()
        p.join()
    print 'All subprocesses done.'
