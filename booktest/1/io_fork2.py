import os
from multiprocessing import Process
def run_proc(name):
    print 'Child process %d (%s) Running' %(name, os.getpid())
if __name__ == '__main__':
    print 'Parent process %s.' %(os.getpid())
    for i in range(5):
        p = Process(target=run_proc, args=(i,))
        print 'Process will start.'
        p.start()
        p.join()
        print 'Process end.'



import os
from multiprocessing import Process
def run_proc(xx):
    print '123%s'%(xx)
if __name__ == '__main__':
    print 'Parent process %s.' %(os.getpid())
    for i in range(3):
        p = Process(target=run_proc, args=('tangq',))
        print 'Process will start.'
        p.start()
        p.join()
        print 'Process end.'