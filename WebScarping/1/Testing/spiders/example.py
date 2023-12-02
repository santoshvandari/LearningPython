import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["test.com"]
    start_urls = ["https://test.com"]

    def parse(self, response):
        pass
