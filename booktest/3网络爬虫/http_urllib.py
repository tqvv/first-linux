#encoding:utf-8
import urllib2
#response =urllib2.urlopen('http://www.zhihu.com')
#html=response.read()
#print html
#搞不懂先用Request的作用？
## 在get方法时可以直接用url，post要先用request把请求格式化
user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
referer='https://www.zhihu.com'
request = urllib2.Request('http://www.zhihu.com')
request.add_header('User-Agent',user_agent)
request.add_header('Referer',referer)
print request
#request = 'http://www.zhihu.com'
response =urllib2.urlopen(request)
html=response.read()
print html

