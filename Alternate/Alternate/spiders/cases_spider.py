# -*- coding: utf-8 -*-
import scrapy

from Alternate.items import CasesItem

class CasesSpider(scrapy.Spider):
    name = "cases"
    allowed_domains = ["alternate.nl"]
    start_urls = [
    	# behuizingen
        "http://www.alternate.nl/html/product/listing.html?filter_5=&filter_4=&filter_3=&filter_2=&filter_1=&size=500&bgid=8148&lk=9309&tk=7&navId=2436#listingResult",
        ]
    def parse(self, response):
        for sel in response.xpath('//div[@class="listRow"]'):
            item = CasesItem()
            item['title'] = ''.join(sel.xpath('a/span/span/h2/span/span/text()').extract())
            #only do this one if it's available
            item['link'] = ''.join(sel.xpath('div/a/@href').extract())
            item['price'] = ''.join(sel.xpath('div[@class="waresSum"]/p/span/text()').extract())
            yield item

