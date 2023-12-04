import scrapy
from scrapy_playwright.page import PageMethod
from pathlib import Path



class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['https://www.nepsealpha.com/nepse-data']
    start_urls = ['http://https://www.nepsealpha.com/nepse-data/']

    def start_requests(self):
       yield scrapy.Request(self.start_urls,
                            meta=dict(
                                playwright=True,
                                playwright_include_page=True,
                                playwright_page_methods=[
                                    # This where we can implement scrolling if we want
                                    PageMethod('wait_for_selector', 'table.table')
                                ]
                            )
                            )

    def parse(self, response):
        tabledata= response.css('table.table tbody tr')
        for data in tabledata:
            symbol = data.css('td:nth-child(2) a::text').get()
            ltp = data.css('td:nth-child(10) span::text').get()
            with open('nepsedata.txt', 'a') as f:
                f.write(f'Symbol: {symbol}\nLast Price: {ltp}\n\n\n')
