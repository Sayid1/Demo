#/bin/usr/python3
# -*- coding:utf-8 -*-
#__author__ = 'Sayid'


import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://',
        'http://'
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract()
            }