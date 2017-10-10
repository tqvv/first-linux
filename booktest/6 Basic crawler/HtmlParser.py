#coding:utf-8
import re
import urlparse
from bs4 import BeautifulSoup
class HtmlParser(object):
    def parser(self,page_url,html_cont):
        #用于解析网页内容，抽取URL和数据
        #param page_url 下载页面的URL
        #param html_count 下载的网页内容
        if page_url is None or html_cont is None:
            return
        else:
            print 'page_url = ',page_url
            #print 'html_cont',html_cont
            soup = BeautifulSoup(html_cont,'html.parser')
            #print 'soup= ',soup
            new_urls= self._get_new_urls(page_url,soup)
            new_data= self._get_new_data(page_url,soup)
            print "new_urls,new_data=",new_urls,new_data
            return new_urls,new_data
    def _get_new_urls(slef,page_url,soup):
        #抽取新的URL集合
        #param page_url下载页面的URL
        #param soup
        #return 返回新的URL集合
        new_urls=set()
        #抽取符合要求的a标记
        links = soup.find_all('a',href=re.compile(r'.*/view/\d+\.htm'))
        print "links =" ,links
        #提取href属性
        for link in links:
            new_url = link['href']
            print 'new_urls = ',new_url
            print 'page_url=',page_url
        #拼接完整网址
            new_full_url = urlparse.urljoin(page_url,new_url)
            print 'new_full_url=',new_full_url
            new_urls.add(new_full_url)

        return new_urls
    def _get_new_data(self,page_url,soup):
        #抽取有效数据
        #param page_url 下载页面的url
        #param soup:
        #return返回有效数据
        data={}
        data['url']=page_url
        title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title']=title.get_text()
        summary=soup.find('div',class_='lemma-summary')
        data['summary']=summary.get_text()
        return data