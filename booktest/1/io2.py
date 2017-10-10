import os
try:
    import cPickle as pickle
except ImportError:
    import pickle
d = dict(url='index.html',title='122',content='222')
#print pickle.dumps(d)
f=open(r'c:\dump.txt','wb')
pickle.dump(d,f)
f.close()
f=open(r'c:\dump.txt','rb')
print d
#f.closed
#with open(r'c:\dump.txt','r') as f2:
 #   print f2.read()
f=open(r'c:\dump.txt','rb')
import os
if __name__ == '__main__':
    getpid = os.getpid()
    print getpid