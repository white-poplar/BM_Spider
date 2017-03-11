#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# @Date    : 2017-03-07 17:19:47
# @Author  : poplar. (BYH5566@gmail.com)
# @Link    : http://white-poplar.github.io
# @Version : 1.0α

import sys
import scrapy
reload(sys)
sys.setdefaultencoding( "utf-8" )


class OneSpider(scrapy.spiders.Spider):
    name = "One"
    # 搜索域名范围
    allowed_domains = ["http://www.fixsub.com"]
    start_urls = ["http://www.fixsub.com/我们的作品?cat=fix日语社"]

    def parse(self, response):
        # filename = "fix_RJ.html"
        # open(filename, 'wb').write(response.body)
        
        for drama in response.xpath('//div[@class="pg-item"]'):
            
            print(drama)

            drama_title = drama.xpath('div[@class="pg-details"]/h2/text()').extract()
            # drama_img = drama.xpath('img[@src]/text()').extract()

            print(drama_title)
            # print(drama_img)
