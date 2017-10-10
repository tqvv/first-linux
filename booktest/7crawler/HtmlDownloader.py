#coding:utf-8
import requests
class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None
        else:
            user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;WindowsNT)'
            headers = {'User-Agent': user_agent}
            r = requests.get(url, headers=headers)
            if r.status_code==200:
                r.encoding='utf-8'
                return r.text
            else:
                return None
                print 'down none'
