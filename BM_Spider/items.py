# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BmSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DramaItem(scrapy.Item):
    title = scrapy.Field()
    img   = scrapy.Field()
    link  = scrapy.Field()
    