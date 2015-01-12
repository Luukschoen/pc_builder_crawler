# -*- coding: utf-8 -*-
import scrapy

from Alternate.items import RamddrItem

class Ram_ddr2Spider(scrapy.Spider):
    name = "ramddr2"
    allowed_domains = ["alternate.nl"]
    start_urls = [
        #DDR2
        "http://www.alternate.nl/html/product/listing.html?navId=11554&tk=7&lk=9312",
        ]
    def parse(self, response):
        for sel in response.xpath('//div[@class="listRow"]'):
            item = RamddrItem()
            item['title'] = ''.join(sel.xpath('a/span/span/h2/span/span/text()').extract())
            item['link'] = ''.join(sel.xpath('div/a/@href').extract())
            item['price'] = ''.join(sel.xpath('div[@class="waresSum"]/p/span/text()').extract())
            yield item


