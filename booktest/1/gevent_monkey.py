#coding:utf-8
from gevent import monkey;
#monkey.patch_all()
import gevent
import urllib2
def run_task(url):
    print 'Vistit---->%s'%url
    try:
        response = urllib2.urlopen(url)
        data = response.read()
        print '%s bytes received from %s'%(data,url)
    except Exception,e:
        print e
if __name__ == '__main__':
    urls = ['https://github.com/','https://www.python.org','https://www.cnblogs.com']
    greenlets = [gevent.spawn(run_task,url) for url in urls]
    gevent.joinall(greenlets)

