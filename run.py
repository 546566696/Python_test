# -*- coding:utf-8 -*-

import urllib2
import re

url = "http://news.upc.edu.cn/sdyw/"
response = urllib2.urlopen(url)
html = response.read()

#跟据正则表达式抓取内容

r=re.compile(r"<a href='/(?P<Date>.{9}).*' target='_blank' title='(?P<Title>.+)' alt='.*</a>")
news = r.findall(html)



for i in range(len(news)):
	date = news[i][0]
	title = news[i][1]
	print title +" "+ date



