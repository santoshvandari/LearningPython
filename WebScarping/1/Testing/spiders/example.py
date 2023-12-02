import scrapy
from pathlib import Path

# https://www.nepalstock.com/today-price

class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["test.com"]
    start_urls = ["https://test.com"]

    def parse(self, response):
        pass
