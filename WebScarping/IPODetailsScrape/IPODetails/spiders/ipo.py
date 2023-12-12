import scrapy,asyncio
from pathlib import Path
from scrapy_playwright.page import PageMethod

class IpoSpider(scrapy.Spider):
    name = 'ipo'
    
    def start_requests(self):
        yield scrapy.Request('https://sarallagani.com/investment-opportunity',
                            meta=dict(
                                playwright=True,
                                playwright_include_page=True,
                                playwright_page_coroutines=[
                                    PageMethod('wait_for_selector', 'table tbody.ant-table-tbody')
                                ]
                        ))

    async def parse(self, response):
        filename = "data.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

        # Wait for additional time to ensure dynamic content is fully loaded
        loop=asyncio.get_event_loop()
        asyncio.set_event_loop(loop)
        await loop.run_until_complete(asyncio.sleep(5))  # Adjust the sleep duration as needed

        # Extract table data
        tabledata = response.css('table tbody.ant-table-tbody tr')

        # Write data to a text file
        with open('data.txt', 'w') as f:
            for row in tabledata:
                name = row.css('td:nth-child(1)::text').get()
                opening = row.css('td:nth-child(5)::text').get()
                closing = row.css('td:nth-child(6)::text').get()
                status = row.css('td:nth-child(7)::text').get()
                f.write(f'Name: {name}\nOpening Price: {opening}\nClosing Price: {closing}\nStatus: {status}\n\n')
