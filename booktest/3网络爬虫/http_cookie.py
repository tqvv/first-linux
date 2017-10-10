#coding:utf-8
import urllib2
import cookielib
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://www.zhihu.com')
for item in cookie:
    print item.name +':'+item.value

print '第二段信息'
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie','email='+ "tqvv@163.com"))
req = urllib2.Request('https://www.zhihu.com/')
response = opener.open(req)
for item in response.read():
    print item
print response.headers
retdata = response.read()