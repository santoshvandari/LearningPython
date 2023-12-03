import scrapy
from scrapy_playwright.page_coroutines import PageCoroutine

class ExampleSpider(scrapy.Spider):
    name = "example"
    scrapeurl = 'https://www.nepalstock.com/today-price'

    def start_requests(self):
        yield scrapy.Request(self.scrapeurl, 
                            meta=dict(
                                playwright=True,
                                playwright_include_page=True,
                                playwright_page_coroutines=[
                                    PageCoroutine('wait_for_selector', 'div.table-responsive')
                                ]
                            )
                            )

    async def parse(self, response):
        # Extract data from each row in the table
        rows = response.css('.table__lg tbody tr')
        for row in rows:
            data = {
                'column1': row.css('td:nth-child(1)::text').get(),
                'column2': row.css('td:nth-child(2)::text').get(),
                # Add more columns as needed
            }
            yield data

        # Optionally, you can save the HTML to a file
        with open('test.html', 'w', encoding='utf-8') as file:
            file.write(response.text)
