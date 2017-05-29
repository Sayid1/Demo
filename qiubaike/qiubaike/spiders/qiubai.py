# -*- coding: utf-8 -*-
import scrapy


class QiubaiSpider(scrapy.Spider):
    name = "qiubai"
    allowed_domains = ["www.qiushibaike.com"]
    start_urls = ['http://www.qiushibaike.com/']

    def parse(self, response):
        print(response.xpath("//div[@class='content']").extract())
