#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# @Date    : 2017-03-07 17:19:47
# @Author  : poplar. (BYH5566@gmail.com)
# @Link    : http://white-poplar.github.io
# @Version : 1.0α


import scrapy
import re
import urllib

# import sys
# reload(sys)
# sys.setdefaultencoding( "utf-8" )


class OneSpider(scrapy.Spider):
    name = "One"
    # 搜索域名范围
    allowed_domains = ["http://www.fixsub.com"]
    start_urls = [
        "http://www.fixsub.com/我们的作品?cat=fix日语社", 
        "http://www.fixsub.com/我们的作品?cat=fix法语社"
    ]

    def parse(self, response):
        # filename = response.url.split('/')[-1]. + '.html'
        

        '''

            fix%E6%97%A5%E8%AF%AD%E7%A4%BE.html
            fix鏃ヨ绀?html
            fix日语社.html
            fix%E6%B3%95%E8%AF%AD%E7%A4%BE.html
            fix娉曡绀?html
            fix法语社.html
            
        '''
        
        filename = re.findall(r'=(.+)', response.url)[0] + '.html'
        filename = urllib.unquote(filename)
        filename = filename.decode('utf8')  # fix%E6%97%A5%E8%AF%AD%E7%A4%BE
        with open(filename, 'wb') as f:
            f.write(response.body)
            
