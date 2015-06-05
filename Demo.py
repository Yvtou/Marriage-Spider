# -*- coding: utf-8 -*-

__author__ = 'Yvtou'

import urllib2

request = urllib2.Request("http://www.i520.org.tw/products-324.html")
response = urllib2.urlopen(request)

print response.read().decode('utf-8', 'ignore').encode('gbk','ignore')

