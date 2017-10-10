#encode:uft-8
import urllib2
try:
    response = urllib2.urlopen('http://www.google.com',timeout=2)
    print response.read()
except urllib2.HTTPError as err:
    if hasattr(err,'code'):
       print 'Errcode:',err.code
       