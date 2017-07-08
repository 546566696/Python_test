# -*- coding:UTF-8 -*-
#import urllib
import urllib2

def download(url, user_agent:'wswp', num_retries = 2):
	print "Downloading:", url
	headers = ('User-agent': user_agent)
	request = urllib2.Request(url, headers = headers)
	
	try:
		html = urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		print "Download error:", e.reason
		html = None
	return html
 
