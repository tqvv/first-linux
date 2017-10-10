#coding:utf-8
import urllib2,urllib
url = "http://ems.cmbchina.com/login"
postdata = {'username':'qiye','password':'qiye_pass'}
data = urllib.urlencode(postdata)
req = urllib2.Request(url,data)
response = urllib2.urlopen(req)
html = response.read()