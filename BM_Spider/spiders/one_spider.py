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
    allowed_domains = ["http://www.liaoxuefeng.com"]
    start_urls = ["http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"]

    def parse(self, response):
        filename = "a.html"
        open(filename, 'wb').write(response.body)
