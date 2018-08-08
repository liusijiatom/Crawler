# -*- coding: utf-8 -*-
import scrapy


class KugouSpider(scrapy.Spider):
    name = 'kugou'
    allowed_domains = ['www.iqiyi.com']
    start_urls = ['http://list.iqiyi.com/www/1/1----------------iqiyi--.html']

    def parse(self, response):
        lis=response.xpath("//ul[@class='site-piclist site-piclist-180236 site-piclist-auto']/li/div/div/p/a/@title").extract()
        for li in lis:
            print(li)
    
    