#coding:utf-8
#成功运行
import urllib2
proxy = urllib2.ProxyHandler({'http':'sandokan.uy.ibm.com:8080'})
opener = urllib2.build_opener(proxy,)
response =opener.open('http://www.google.com/')
print response.read()
