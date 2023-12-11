import scrapy


class IpoSpider(scrapy.Spider):
    name = 'ipo'
    allowed_domains = ['https://investornepal.com/upcoming-ipo/']
    start_urls = ['http://https://investornepal.com/upcoming-ipo//']

    def parse(self, response):
        pass
