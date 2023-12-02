import scrapy
from pathlib import Path

# https://www.nepalstock.com/today-price

class ExampleSpider(scrapy.Spider):
    name = "example"
    def start_requests(self):
        urls = [
            "http://books.toscrape.com/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        filename = f"booksdata.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
