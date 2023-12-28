import scrapy
from scrapy_playwright.page import PageMethod
from pathlib import Path



class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.sharesansar.com']
    start_urls = 'https://www.sharesansar.com/live-trading'

    def start_requests(self):
        yield scrapy.Request('https://www.sharesansar.com/live-trading',
                            meta=dict(
                                playwright=True,
                                playwright_include_page=True,
                                playwright_page_methods=[
                                    # This where we can implement scrolling if we want
                                    PageMethod('wait_for_selector', 'table#headFixed'),
                                ]
                            )
                            )

    def parse(self, response):
        # with open('nepsedata.html', 'w') as f:
        #     f.write(response.body.decode('utf-8'))

        tabledata= response.css('table#headFixed tbody tr')
        for data in tabledata:
            symbol = data.css('td:nth-child(2) a::text').get()
            ltp = data.css('td:nth-child(3)::text').get()
            with open('nepsedata.txt', 'a') as f:
                f.write(f'Symbol: {symbol}\nLast Price: {ltp} \n\n\n')
