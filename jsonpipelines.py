# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
from openpyxl import Workbook
class MyscrapydemoItem(object):
    def process_item(self, item, spider):
        jsonInfo=json.dumps(dict(item),ensure_ascii=False)
        with open('musicInfo.json','a',encoding="utf-8") as wrStream:
            wrStream.write(jsonInfo+"\n")
        return item
class ExcMyscrapydemoItem(object):
    def __init__(self):
        self.wb=Workbook()
        self.wc=self.wb.active
        self.wc.append(['电影名称 ','评分'])
    def process_item(self, item, spider):
        line=[item['name'],item['score']]
        self.wc.append(line)
        self.wb.save('movie.csv')
        return item
        
        
