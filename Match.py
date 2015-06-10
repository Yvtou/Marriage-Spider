# -*- coding: utf-8 -*-

__author__ = 'Owen'


import urllib2
import re
from openpyxl import Workbook

#建立工作表格
wb = Workbook()
ws = wb.active
ws.title = "test"

#设置需要抓取的页面范围
for pageIndex in range(3, 10):
    print u'正在抓取第' + str(pageIndex) + u'位的信息……'
    #抓取网页的地址
    url = 'http://www.i520.org.tw/products-' + str(pageIndex) + '.html'
    request = urllib2.Request(url)
    #处理Http和Url错误
    try:
        response = urllib2.urlopen(request)
    #若有错误，显示错误类型
    except urllib2.URLError, e:
        if hasattr(e, 'code'):
            print u'服务器无法完成此次请求'
            print u'错误代码：', e.code
        elif hasattr(e, 'reason'):
            print u'无法连接到服务器'
            print u'原因： ', e.reason
    #若无错误，则开始抓取
    else:
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
        wb.save('temp.xlsx')
        #注意！先保存此表格中数据再进行下次抓取，否则数据会被覆盖！
else:
    print u'抓取结束'
