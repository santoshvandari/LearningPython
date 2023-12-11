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
        file = open("bookdata.txt", "a")
        # for bookcard in bookcards:
        # for row in tablebody:
        for row in tablebody:
            # print("**********")
            # print(row)
            symbol = row.css("td:nth-child(1)::text").get()
            fullname= row.css("td:nth-child(2)::text").get()
            totalunit= row.css("td:nth-child(3)::text").get()
            openprice= row.css("td:nth-child(5)::text").get()
            closeprice= row.css("td:nth-child(6)::text").get()
            # title = table.css("h3 a::attr(title)").get()
            # price = table.css(".price_color::text").get()
            # rating = table.css(".star-rating::attr(class)").get().split(" ")[-1]+" stars"
            if(openprice is not None and closeprice is not None):
                file.write(f"Symbol: {symbol}\nFull Name: {fullname}\nTotal Unit: {totalunit}\nOpen Price: {openprice}\nClose Price: {closeprice}\n\n\n")
        file.close()

