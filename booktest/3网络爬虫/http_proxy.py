#coding:utf-8
#该办法有问题
import urllib2
proxy = urllib2.ProxyHandler({'https':'sandokan.uy.ibm.com:8080'})
opener = urllib2.build_opener([proxy,])
urllib2.install_opener(opener)
response =urllib2.urlopen('https://www.google.com/')
print response.read()
