# encoding=utf-8
from bs4 import  BeautifulSoup
from lxml import etree
import re
soup = BeautifulSoup(open('index.html'),"lxml")
#print soup.prettify()
print "*****"*10
# select = css 选择器
print soup.select('a[href*="baidu"]')

# lxml for et

html_str ="""
<html>
<head>
    <title>The Dormouse's story</title>
</head>
<body>
<p class = 'title'>
<b>
    The Dormouse's story
</b>
</p>
<p class='story'>
once upon atime there wer three lixxx
<a  href="http://www.baidu1.com" class = "sister" id="link1">
    thise
    <!---ELSIE---->
</a>
<a href="http://www.baidu2.com" class = "sister" id="link2">
    <!---ELCIE---->
</a>
<a  href="http://www.baidu3.com" class = "sister" id="link3">
  TILLIE
</a>
AND THEY LIEV AT THE bottom of wall
</p>
<p class = 'story'>
........
    dfdfsfddsfa
</p>>


</body>
</html>
"""
#html = etree.parse('index.html')
#result = etree.tostring(html,preetty_print=True)
html = etree.HTML(html_str)
result =  etree.tostring(html)
#print result
print html.xpath(".//*[@class='sister']/@href")