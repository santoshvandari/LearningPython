# This is Working Code. It will scrape data from nepalstock.com and save it in nepsedata.txt file
    
import scrapy
from scrapy_playwright.page import PageMethod
from pathlib import Path

class PwspiderSpider(scrapy.Spider):
    name = 'ipo'
    allowed_domains = ['sarallagani.com']
    start_urls = ['https://sarallagani.com/investment-opportunity']

    def start_requests(self):
        yield scrapy.Request('https://sarallagani.com/investment-opportunity',
                            meta=dict(
                                playwright=True,
                                playwright_include_page=True,
                                playwright_page_methods=[
                                    # This where we can implement scrolling if we want
                                    PageMethod('wait_for_selector', 'table tbody.ant-table-tbody'),
                                ]
                            )
                            )

    async def parse(self, response):
        filename = f"data.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        # data= response.css('table.table tbody tr td:nth-child(3)::text').get()
        # print(data)

        tabledata= response.css('table tbody.ant-table-tbody tr')
        for data in tabledata:
            symbol = data.css('td:nth-child(1)::text').get()
            openingdate = data.css('td:nth-child(5)::text').get()
            closingdate = data.css('td:nth-child(6)::text').get()
            status = data.css('td:nth-child(7) div::text').get()
            with open('nepsedata.json', 'a') as f:
                f.write(f'Name: {symbol}\nOpening Price: {openingdate}\nClosing Price: {closingdate}\nStatus: {status}\n\n\n')







# password of Database: rnR0uiDqNVWiBL1C















