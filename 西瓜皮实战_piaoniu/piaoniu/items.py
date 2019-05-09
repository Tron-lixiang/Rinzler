# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PiaoniuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    rank = scrapy.Field()
    time=scrapy.Field()
    price = scrapy.Field()
    weizhi = scrapy.Field()
    conn =scrapy.Field()
    city=scrapy.Field()
