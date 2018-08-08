# -*- coding: utf-8 -*-
# import scrapy
# from myscrapyDemo.items import MyscrapydemoItem
# from myscrapyDemo import DBUtil

# class JidongSpider(scrapy.Spider):
#     name = 'jidong'
#     allowed_domains = ['www.kankan.com/']
#     start_urls = ['http://movie.kankan.com/type,order,genre/movie,update,Action/']
#     for i in range(1,1):
#         start_urls.append("http://movie.kankan.com/type,order,genre/movie,update,Action/page%d/"%i)

#     def parse(self, response):
#         #lis=response.xpath("//ul[@class='clear_fix']").extract()
#         lis=response.xpath("//ul[@class='movielist']/li/p/a/@title").extract()
#         lns=response.xpath("//ul[@class='movielist']/li/p[@class='movielist_tt']/em[@class='score']/text()").extract()
#         #print('---------------------------',lns)
#         items=[]
#         for (li,ln) in zip(lis,lns):

#             musicname=MyscrapydemoItem()
#             sql ="select name from movies where name='"+lis+"' "
#             DBUtil.execute(sql)
#             print(DBUtil.execute(sql))
#             print(lis)
#             if DBUtil.execute(sql) != lis:
#                 musicname['name']=li
#                 musicname['score']=ln
#                 items.append(musicname)
#                 yield musicname
#         return items
import scrapy
from myscrapyDemo.items import MyscrapydemoItem
from myscrapyDemo import DBUtil

class JidongSpider(scrapy.Spider):
    name = 'jidong'
    allowed_domains = ['www.kankan.com/']
    start_urls = ['http://movie.kankan.com/type,order,genre/movie,update,Action/']
    for i in range(1,2):
        start_urls.append("http://movie.kankan.com/type,order,genre/movie,update,Action/page%d/"%i)
        print(start_urls.append("http://movie.kankan.com/type,order,genre/movie,update,Action/page%d/"%i))
    def parse(self, response):
        
        detail = response.xpath("//ul[@class='movielist']/li")
        print("数目     ",len(detail))
        # print('div',detail)
        for info in detail:
            musicname=MyscrapydemoItem()

            moviesname=info.xpath("p[@class='movielist_tt']/a/text()").extract()[0]
            print(moviesname)
            score=info.xpath("p[@class='movielist_tt']/em[@class='score']/text()").extract()[0]
            # bookItem['URL']=URL
            # yield bookItem
            sql="select name from movies where name='"+moviesname+"' "
            DBUtil.execute(sql)
            # print(DBUtil.execute(sql))
            a=(moviesname,)
            # print(a)
            if DBUtil.execute(sql)!=a:
                musicname['name']=moviesname
                musicname['score']=score
                yield musicname
                
        pass

     