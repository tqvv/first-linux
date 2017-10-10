#coding:utf-8
class URLManager(object):
    def __init__(self):
        self.new_urls = set()#未爬取的URL集合
        self.old_urls = set() #已爬取的URL集合
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
        self.old_urls.add(new_url)
        return  new_url
    def add_new_url(self,url):
        #...
        #将新的URL添加到未爬取的URL集合中
        #param url:
        #return
        if url is None:
            return
        else:
            if (url not in self.new_urls and url not in self.old_urls):
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

