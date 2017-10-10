#coding:utf-8
import requests
import chardet
#r = requests.get('http://www.baidu.com')
#print r.content
#print r.text.encode('utf-8')
#print r.encoding
#r.encoding = 'utf-8'
#print r.textG
#r2 = requests.get('http://www.baidu.com')
#ostdata = {'name':'tqvv','passowrd':'tqvv'}
#r2 = requests.head('http://www.baidu.com')
#print chardet.detect(r2.content)
#r2.encoding =chardet.detect(r2.content)['encoding']
#print r2.text
#r3 = requests.get('http://www.zhihu.com',stream=True)
#r3.encoding =chardet.detect(r3.content)['encoding']
#print r3.raw.read(1000)
#r = requests.get('http://www.baidu.com')
# if r.status_code == requests.codes.ok:
#     print  r.status_code
#     print requests.codes.ok
#     print r.headers
#     print 'content-type====='+r.headers.get('content-type')
#     print 'allheader-content-type=='+r.headers['content-type']
# else:
#     r.raise_for_status()



# user_agent = 'Mozila/4.0(compatible;MSIE5.5;Windows NT)'
# headers = {'User-Agent':user_agent}
# r = requests.get('http://www.baidu.com',headers=headers)
# for cookie in r.cookies.keys():
#     print cookie + ':' + r.cookies.get(cookie)

#Session
#常用
# loginUrl = 'https://www.baidu.com/'
# s = requests.Session()
# r = s.get(loginUrl,allow_redirects=True)
# datas = {'name':'18620328812','passwd':'123'}
# r = s.post(loginUrl,data=datas,allow_redirects=True)
# print r.content


# r = requests.get('http://github.com',allow_redirects=False,timeout=1)
# print r.url
# print r.status_code
# print r.history

proxies = {"http":"sandokan.uy.ibm.com:8080","https":"sandokan.uy.ibm.com:8080"}
requests.get('https://www.google.com/',timeout =2,proxies=proxies )
print r.content



