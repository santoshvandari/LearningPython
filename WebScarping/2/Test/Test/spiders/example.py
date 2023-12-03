# This is Working Code. It will scrape data from nepalstock.com and save it in nepsedata.txt file
    
# import scrapy
# from scrapy_playwright.page import PageMethod
# from pathlib import Path

# class PwspiderSpider(scrapy.Spider):
#     name = 'example'
#     allowed_domains = ['www.nepalstock.com']
#     start_urls = ['https://www.nepalstock.com/today-price']

#     def start_requests(self):
#         yield scrapy.Request('https://www.nepalstock.com/today-price',
#                             meta=dict(
#                                 playwright=True,
#                                 playwright_include_page=True,
#                                 playwright_page_methods=[
#                                     # This where we can implement scrolling if we want
#                                     PageMethod('wait_for_selector', 'table.table')
#                                 ]
#                             )
#                             )

#     async def parse(self, response):
#         # filename = f"nepsedata.html"
#         # Path(filename).write_bytes(response.body)
#         # self.log(f"Saved file {filename}")

#         tabledata= response.css('table.table tbody tr')
#         for data in tabledata:
#             symbol = data.css('td:nth-child(2) a::text').get()
#             ltp = data.css('td:nth-child(10) span::text').get()
#             with open('nepsedata.txt', 'a') as f:
#                 f.write(f'Symbol: {symbol}\nLast Price: {ltp}\n\n\n')







# This is not Working Code. It will scrape data from nepalstock.com and save it in nepsedata.txt file
import scrapy
from scrapy_playwright.page import PageMethod
from pathlib import Path


class PwspiderSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.nepalstock.com']
    start_urls = ['https://www.nepalstock.com/today-price']

    def start_requests(self):
        yield scrapy.Request('https://www.nepalstock.com/today-price',
                            meta=dict(
                                playwright=True,
                                playwright_include_page=True,
                                playwright_page_methods=[
                                    # Wait for the pagination controls to load
                                    PageMethod('wait_for_selector', 'pagination-controls'),
                                    # Extract the next page URL
                                    PageMethod('evaluate', 'document.querySelector("pagination-controls").querySelector("a.pagination-next").getAttribute("href")'),
                                    # Check if there's a next page
                                    PageMethod('evaluate', '!!document.querySelector("a.pagination-next").getAttribute("href")')
                                ]
                            )
                            )

    async def parse(self, response):
        next_page_url = response.meta.get('next_page_url')

        # Extract data from the current page
        tabledata = response.css('table.table tbody tr')
        for data in tabledata:
            symbol = data.css('td:nth-child(2) a::text').get()
            ltp = data.css('td:nth-child(10) span::text').get()

            with open('nepsedata.txt', 'a') as f:
                f.write(f'Symbol: {symbol}\nLast Price: {ltp}\n\n\n')

        # Follow the next page if it exists
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), meta=response.meta)








