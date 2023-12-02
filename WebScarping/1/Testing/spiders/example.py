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
        bookcards=response.css(".product_pod")
        file = open("bookdata", "a")
        for bookcard in bookcards:
            title = bookcard.css("h3 a::attr(title)").get()
            price = bookcard.css(".price_color::text").get()
            rating = bookcard.css(".star-rating::attr(class)").get().split(" ")[-1]+" stars"
            file.write(f"Title: {title}\nPrice: {price}\nRating: {rating}\n\n\n")
        file.close()




