#coding:utf-8
import DataOutput
import HtmlDownloader
import HtmlParser
import URLManager
import random, time
from multiprocessing import Process,Queue
from multiprocessing.managers import BaseManager
class SpiderWork(object):
    def __init__(self):
        BaseManager.register('get_task_queue')
        BaseManager.register('get_result_queue')
        server_addr = '127.0.0.1'
        print('Connect to server%s.....'%server_addr)
        self.m = BaseManager(address=(server_addr,8001),authkey='baike')
        self.m.connect()
        self.task = self.m.get_task_queue()
        self.result = self.m.get_result_queue()
        self.downloader = HtmlDownloader.HtmlDownloader()
        self.parser = HtmlParser.HtmlParser()
        print ('init finish')
    def crawl(self):
        while(True):
            try:
               if not self.task.empty():
                   url = self.task.get()
               else:
                   if url =='end':
                       print '控制节点通知爬虫节点停止工作'
                       self.result.put({'new_urls':'end','data':'end'})
                       return
                   else:
                       try:
                           print '爬虫节点正在解析:%s'%url.encode('utf-8')
                           content = self.downloader.download(url)
                           new_urls,data =self.parser.parser(url,content)
                           self.result.put({'new_urls':new_urls,'data':data})
                       except EOFError,e:
                           print '连接工作节点失败'
                           return
            except Exception,e:
                print e
                print "Crawl Failed"
if __name__ =="__main__":
    spider_man = SpiderWork()
    #spider_man.crawl("http://seputu.com")
    spider_man.crawl()