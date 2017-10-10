from bs4 import  BeautifulSoup
import re
soup = BeautifulSoup(open('index.html'),"lxml")
#print soup
#print soup.name
#print soup.title.name
# print soup.p.b.string
# print type(soup.p.b.string)
# print soup.p.b.text
# print type(soup.p.b.text)
# print soup.p['class']
# print soup.p.attrs
# print soup.head.contents
# print soup.head.contents[1].string
# print type(soup.head.contents)
# for string in soup.stripped_strings:
#     print repr(string)
# print soup.title
# print soup.title.parent.name
#print soup.a
# for parent in soup.a.parents:
#     if parent is None:
#         print parent
#     else:
#         print parent.name
#html
# print 'soup.p.text=',soup.p.string
# print 'soup.p.next_sibling=',soup.p.next_sibling
# print 'soup.a.prev_sibling=',soup.p.prev_sibling
# print 'soup.p.next_sibling2=',soup.p.next_sibling.next_sibling
#
print soup.prettify()
# for sibling in soup.a.next_siblings:
#     print repr(sibling)
# print soup.head
#
# print soup.head.next_element
# print soup.head.next_element.next_element
#print soup.head.next_element.next_element.next_element
# print soup.head.next_element.next_element.next_element.next_element
# # is import1
# for element in soup.head.next_elements:
#     print repr(element)
print "*****"*10
#print soup.find_all(['b','p'])
#print soup.find_all(re.compile('^b'))
# for tag in soup.find_all(re.compile('^a')):
#     print str(tag)
# print "*****" * 10
# for tag in soup.find_all(True):
#     print str(tag.name)
print soup.find_all(clsss ="sister",text=re.compile('this'))
print soup.find_all(text=re.compile('this'))


