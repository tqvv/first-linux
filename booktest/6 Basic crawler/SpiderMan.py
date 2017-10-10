#coding:utf-8
import DataOutput
import HtmlDownloader
import HtmlParser
import URLManager
class SpiderMan(object):
    def __init__(self):
        self.downloader = HtmlDownloader.HtmlDownloader()
        self.parser = HtmlParser.HtmlParser()
        self.output = DataOutput.DataOutput()
        self.manager = URLManager.URLManager()
    def crawl(self,root_url):
        print "root_url1=" ,root_url
        self.manager.add_new_url(root_url)
        print "self.manager.has_new_url0()= ", self.manager.has_new_url()
        while(self.manager.has_new_url() and self.manager.old_url_size()<100):
            print "self.manager.has_new_url()= ", self.manager.has_new_url()
            print self.manager.old_url_size()
            try:
                new_url = self.manager.get_new_url()
                print "new_url 1= ",new_url
                html = self.downloader.download(new_url)
                #print "html = " ,html
                new_urls,data = self.parser.parser(new_url,html)
                print "new_urls,new_data2=", new_urls, data
                print 'data 110 =',data
                print 'data 120 =',data
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print "已经抓取%s个链接"%self.manager.old_url_size()
            except:
                print "self.manager.has_new_url() ", self.manager.has_new_url()
                print self.manager.old_url_size()
                print "Crawl Failed"
        self.output.output_html()
if __name__ =="__main__":
    spider_man = SpiderMan()
    #spider_man.crawl("http://seputu.com")
    spider_man.crawl("http://baike.baidu.com/view/284853.htm")