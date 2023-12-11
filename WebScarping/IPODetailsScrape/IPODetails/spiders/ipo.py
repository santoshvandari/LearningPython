import scrapy
from pathlib import Path


class IpoSpider(scrapy.Spider):
    name = 'ipo'
    # allowed_domains = ['https://investornepal.com/upcoming-ipo/']
    # start_urls = ['http://https://investornepal.com/upcoming-ipo//']
    url='https://investornepal.com/upcoming-ipo/'
    def start_requests(self):
        yield scrapy.Request(url=self.url)

    def parse(self, response):
        filename = "data.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        table= response.css("#tablepress-UpcomingIPOs")
        tablebody= table.css("tbody tr")
        file = open("bookdata", "a")
        # for bookcard in bookcards:
        for row in tablebody:
            symbol = row.css("td:nth-child(1)")
            fullname= row.css("td:nth-child(2)")
            totalunit= row.css("td:nth-child(3)")
            openprice= row.css("td:nth-child(5)")
            closeprice= row.css("td:nth-child(6)")
            # title = table.css("h3 a::attr(title)").get()
            # price = table.css(".price_color::text").get()
            # rating = table.css(".star-rating::attr(class)").get().split(" ")[-1]+" stars"
            file.write(f"Symbol: {symbol}\nFull Name: {fullname}\nTotal Unit: {totalunit}\nOpen Price: {openprice}\nClose Price: {closeprice}\n\n\n")
        file.close()

