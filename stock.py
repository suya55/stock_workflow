# -*- coding:utf-8 -*-
import locale
import urllib
import json
import unicodedata

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

if len(sys.argv) != 2: 
  exit("Useage : stock.py 카카오")

q = u'%s' % sys.argv[1]
q2 = unicodedata.normalize('NFC', q)
q3 = urllib.quote(q2.encode('utf-8'))

unparsed = urllib.urlopen(u'http://m.stock.naver.com/api/json/search/searchListJson.nhn?keyword=%s&pageSize=30&page=1' % q3).read()

obj = json.loads(unparsed)

elems = []
locale.setlocale(locale.LC_ALL, 'en_US')
for item in obj["result"]["d"]:
  if item["cv"] > 0 :
    arrow = "\033[0;31m▲"
  elif item["cv"] == 0 :
    arrow = "-"
  else :
    arrow = "\033[0;36m▼"
  print u'| %s | \033[0;32m%s\033[0m원(%s%0.2f%%\033[0m %s원) | 거래량 : %s | 전날종가 : %s원 | http://finance.daum.net/item/main.daum?code=%s |' % (item["nm"], locale.format("%d", item["nv"], grouping=True), arrow, item["cr"], locale.format("%d", item["cv"], grouping=True), locale.format("%d", item["aq"], grouping=True), locale.format("%d", item["pcv"], grouping=True),item["cd"])
  
