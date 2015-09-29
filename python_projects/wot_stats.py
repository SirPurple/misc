#! /usr/bin/env python
__author__ = 'Johan Bradvik'

from urllib.request import urlopen

html = urlopen("http://www.google.com/")
print(html)

'''
import urllib.request
url = "http://www.google.com/"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
print (response.read().decode('utf-8')
'''