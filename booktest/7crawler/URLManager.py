#coding:utf-8
import cPickle
import hashlib
class URLManager(object):
    def __init__(self):
        self.new_urls = self.load_progress('new_urls.txt')#未爬取的URL集合
        self.old_urls = self.load_progress('old_urls.txt') #已爬取的URL集合
        print "self.new_urls0 =", self.new_urls
        print "self.old_urls0 =", self.old_urls

    def has_new_url(self):
        #…
        #判断是否由未爬取的URL
        #return:
        #…
        return self.new_url_size()!=0
    def get_new_url(self):
        #…
        #获取未爬取的URL
        #return:
        #…
        new_url = self.new_urls.pop()
        m = hashlib.md5()
        m.update(new_url)
        self.old_urls.add(m.hexdigest()[8:-8])
        return  new_url
    def add_new_url(self,url):
        #...
        #将新的URL添加到未爬取的URL集合中
        #param url:
        #return
        if url is None:
            return
        else:
            m = hashlib.md5()
            m.update(url)
            url_md5 = m.hexdigest()[8:-8]
            if (url not in self.new_urls and url_md5 not in self.old_urls):
                self.new_urls.add(url)
                print "self.new_urls1 =", self.new_urls
    def add_new_urls(self,urls):
        #将新的url添加了未爬去的url集合中
        #param urls URL集合
        if urls is None or len(urls)==0:
            print 'urls =', urls
            return
            for url in urls:
                self.add_new_url(url)
                print 'urls =',urls
    def new_url_size(self):
        #获取未爬去URL集合的大小
        print "len(self.new_urls) = ",len(self.new_urls)
        return len(self.new_urls)
    def old_url_size(self):
        #获取已爬取URL集合的大小
        return len(self.old_urls)
    def save_progress(self,path,data):
        #保存进度
        with open(path,'wb') as f:
            cPickle.dump(data,f)
    def load_progress(self,path):
        try:
            with open(path,'rb') as f:
                tmp = cPickle.load(f)
            print '创建：  create %s'%tmp
            return tmp
        except:
            print '无文件进度，创建： nofile create %s'%path
            return set()


