import scrapy
from scrapy_playwright.page import PageMethod
from pathlib import Path



class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['https://www.nepsealpha.com/nepse-data']
    start_urls = 'https://www.nepsealpha.com/nepse-data/'

    def start_requests(self):
        yield scrapy.Request(self.start_urls,
                            meta=dict(
                                playwright=True,
                                playwright_include_page=True,
                                playwright_page_methods=[
                                    # This where we can implement scrolling if we want
                                    PageMethod('wait_for_selector', 'table#DataTables_Table_0')
                                ]
                            )
                            )

    def parse(self, response):
        tabledata= response.css('table.table tbody tr')
        for data in tabledata:
            symbol = data.css('td:nth-child(1) a::text').get()
            ltp = data.css('td:nth-child(9) span::text').get()
            with open('nepsedata.txt', 'a') as f:
                f.write(f'Symbol: {symbol}\nLast Price: {ltp}\n\n\n')
