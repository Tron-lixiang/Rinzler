# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from piaoniu.items import PiaoniuItem

class TronpiaoniuSpider(RedisSpider):
    name = 'tronpiaoniu'
    allowed_domains = ['www.piaoniu.com']
    redis_key = 'piaoniustart'
    start_urls = ['http://www.piaoniu.com/']
    host = 'http://www.piaoniu.com'
    def parse(self, response):
        menpiao_list = response.xpath('//li[@class="item"]')
        i=0
        for menpiao in menpiao_list:
            menpiao_title = menpiao.xpath('a/@title').extract_first()
            menpiao_conn ='http:' + menpiao.xpath('a/@href').extract()[0]
            menpiao_price=menpiao.xpath('//div[@class="sale-price"]/span[@class="strong"]/text()').extract()[i]
            menpiao_city = response.xpath('//div[@class="city-picker"]/div[@class="city-name"]/text()').extract()
            i += 1
            item = PiaoniuItem()
            item['name']=menpiao_title
            item['conn']=menpiao_conn
            item['price']=menpiao_price
            item['city'] = menpiao_city
            yield scrapy.Request(menpiao_conn,
                                 headers=self.settings['HEADERS'],
                                 callback=self.parse_detail,
                                 meta={'item': item})
        for url in response.xpath('//ul[@class="paginator"]/li[@class="page"]/a/@href').extract():
            yield scrapy.Request(self.host + url,callback=self.parse)
    def parse_detail(self, response):
        item = response.meta['item']
        rank = response.xpath('//div[@class="rank"]/div[@class="num"]/text()').extract_first()
        time = response.xpath('//div[@class="time"]/text()').extract_first()
        name=response.xpath('//div[@class="head"]/div[@class="title"]/text()').extract()
        menpiao_weizhi = response.xpath('//div[@class="main"]/div[@class="desc"]/text()').extract_first()
        item['weizhi'] = menpiao_weizhi
        item['time'] = time
        item['rank'] = rank
        item['name'] = name
        yield item