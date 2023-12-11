import scrapy


class IpoSpider(scrapy.Spider):
    name = 'ipo'
    # allowed_domains = ['https://investornepal.com/upcoming-ipo/']
    # start_urls = ['http://https://investornepal.com/upcoming-ipo//']
    url='https://investornepal.com/upcoming-ipo/'
    def start_requests(self):
        yield scrapy.Request(url=self.url)

    def parse(self, response):
        pass
