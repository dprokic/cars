# -*- coding: utf-8 -*-
import scrapy


class PolovniautomobiliSpider(scrapy.Spider):
    name = 'polovniautomobili'
    allowed_domains = ['www.polovniautomobili.com']
    start_urls = ['https://www.polovniautomobili.com/putnicka-vozila/poslednja24h']

    def parse(self, response):
        title_links = response.css("article.single-classified h3.uk-grid span a")
        prices = response.css("article.single-classified h3.uk-grid span span::text").extract()

        for item in (zip(title_links, prices)):
            title = title_links.css('a::text').extract()[0].strip()
            scraped_info = {
                'title': title,
                'price': item[1].strip()
            }
            yield scraped_info
