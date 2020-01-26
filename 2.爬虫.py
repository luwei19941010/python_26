#-*-coding:utf-8-*-
# Author:Lu Wei
import requests,re
import json

def url_get(num):
    req=requests.get('https://movie.douban.com/top250?start=%s&filter='%num)
    return req.text

pattern='<div class="item">.*?<em class="">(?P<id>/d+)</em>.*?<span class="title">(?P<title>.*?)</span>.*?<span class="rating_num.*?>(?P<score>.*?)</span>.*?<span>(?P<c_num>.*?)人评价</span>'
rex=re.compile(pattern,flags=re.S)


