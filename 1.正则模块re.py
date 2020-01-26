#-*-coding:utf-8-*-
# Author:Lu Wei
import re

# ret=re.sub('\d','D','asdasd124wqe3132w12qe',1)
# print(ret)

# s1='<h1>wahaha</h1>'
# ret=re.search('<(?P<tag>\w+)>(?P<cont>.*?)(</(?P=tag)>)',s1)
# print(ret.group(0))
# print(ret.group('tag'))
# print(ret.group('cont'))
# ret=re.split( '\d+','alex83taibai82luwei19')
# ret=re.split( '(\d+)','alex83taibai82luwei19')#默认自动保留分组中的内容
# print(ret)

def func():
    print(123)
    n=yield 'aaaa'
    print('--->',n)
    yield 'bbbb'
g=func()
g1=next(g)
print(g1)
g2=next(g)
print(g2)