import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['https://www.nepsealpha.com/nepse-data']
    start_urls = ['http://https://www.nepsealpha.com/nepse-data/']

    def start_requests(self):
        return super().start_requests()

    def parse(self, response):
        pass
