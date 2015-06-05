# -*- coding: utf-8 -*-

__author__ = 'Yvtou'


import urllib2
import re
from openpyxl import Workbook

#建立工作表格
wb = Workbook()
ws = wb.active
ws.title = "New Title"

#页面循环
for pageIndex in range(61, 324):
    print u'正在抓取第' + str(pageIndex) + u'位的信息……'
    #抓取网页
    url = 'http://www.i520.org.tw/products-' + str(pageIndex) + '.html'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    #正则匹配，注意中文编码问题
    content = response.read().decode('utf-8')
    pattern = re.compile('<div class="girlInfo">.*?<h2>(.*?)</h2>.*?<ul>.*?<li>(.*?)</li>.*?<li>(.*?)</li>.*?<li>(.*?)</li>.*?<li>(.*?)</li>.*?<li>(.*?)</li>.*?<li>(.*?)</li>.*?<li>(.*?)</li>.*?</ul>',re.S)
    items = re.findall(pattern,content)
    #输出结果
    for item in items:
        print item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7]
        #写入工作表
        for c in range(0,8):
            d = ws.cell(row = pageIndex+1, column = c+1)
            d.value = item[c]
    #储存
    wb.save('balances.xlsx')
else:
    print u'抓取结束'
