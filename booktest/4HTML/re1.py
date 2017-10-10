#coding:utf-8
import re
# compile pattern对象
pattern = re.compile(r'\d+')
result1 = re.match(pattern,'192abc')
if result1:
    print result1.group()
else:
    print 'match failed1'
#match 与rules的nmatch类似
pattern = re.compile(r'[A-Z]+',re.I)
result1 = re.match(pattern,'abc192')
if result1:
    print result1.group()
else:
    print 'match failed2'

#search 类似rules中regmatch
pattern = re.compile(r'\d+')
result1 = re.search(pattern, 'abc192')
if result1:
    print result1.group()
else:
    print 'match failed3'

#split 类似rules中split,但更强大，rules中的多个字符是or，这里and，支持正则分割
pattern = re.compile(r'456')
result1 = re.split(pattern, 'abc456|dddas456|fdsafas')
print result1
#返回子串
pattern = re.compile(r'\d+')
result1 = re.findall(pattern, 'abc456|dddas456|fdsafas')
print result1

#返回迭代对象
pattern = re.compile(r'\d+')
result1 = re.finditer(pattern, 'abc456|dddas456|fdsafas')
for match in result1:
    print match.group()
#re.sub 等于impact replace函数
p = re.compile(r'(P<word1>\w+) (P<word2>\w+)')
#使用名称引用
s ='i say , hello world !'
print p.sub(r'\k<word2>\k<word1>',s)
p= re.compile(r'(\w+) (\w+)')
print p.sub(r'\2 \1',s)
def func(m):
    return m.group(1).title() + ' '+m.group(2).title()
print p.sub(func,s)

#具体练习
s ='abc123ab1233123ctrtrtr123'
pattern = re.compile(r'(\d+)')
print re.sub(pattern,'',s)

s ='abc123ab1233123ctrtrtr123'
pattern = re.compile(r'(\d+)')
print re.subn(pattern,'',s,2)


pattern = re.compile(r'\d+')
result1 = re.search(pattern, 'abc192abcd189')
print '.string = %s xxx'%(result1.string)
print '.re :',result1.re
print '.pos :',result1.pos
print '.endpos :',result1.endpos
print '.lastindex :',result1.lastindex
print '.lastgroup :',result1.lastgroup
#print '.group(1,2) :',result1.group(1,2)
print '.group() :',result1.group()
print '.groupdict() :',result1.groupdict()
print '.start() :',result1.start()
print '.end() :',result1.end()
print '.span() :',result1.span()
# print r"expand" ,result1.expand(r'\2\1\3')