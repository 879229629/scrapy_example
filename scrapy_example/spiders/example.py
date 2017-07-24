# -*- coding: utf-8 -*-
import scrapy
import logging


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['itunes.apple.com']
    start_urls = ['https://itunes.apple.com/rss/customerreviews/page=1/id=874881574/sortby=mostrecent/xml?l=en&&cc=cn']

    def parse(self, response):
        logging.warning("This is a warning %s", response.headers)