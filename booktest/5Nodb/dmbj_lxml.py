# encoding=utf-8
from lxml import etree
import requests
import csv
import re
user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;WindowsNT)'
headers={'User-Agent':user_agent}
r = requests.get('http://seputu.com',headers=headers)
html = etree.HTML(r.text)
mulus = html.xpath('.//*[@class="mulu"]')
rows=[]
for mulu in mulus:
    print "**************"
    h2 = mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
    if len(h2)>0:
        h2_title = h2[0].encode('utf-8')
        #print h2_title
        a_s =  mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            href = a.xpath('./@href')[0].encode('utf-8')
            box_title = a.xpath('./@title')[0]
            pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
            match = pattern.search(box_title)
            if match !=None:
                date = match.group(1).encode('utf-8')
                real_tile = match.group(2).encode('utf-8')
                content= (h2_title,real_tile,href,date.strip())
                rows.append(content)
headers=['title','real_title','href','date']
print rows
with open('qiye.csv','w') as f:
    f_csv = csv.writer(f,delimiter='	')
    #f_csv.writerow(headers)
    f_csv.writerows(rows)
