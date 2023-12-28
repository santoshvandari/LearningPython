import scrapy
from pathlib import Path

# https://www.nepalstock.com/today-price

class ExampleSpider(scrapy.Spider):
    name = "example"
    def start_requests(self):
        urls = [
            "http://books.toscrape.com/catalogue/page-1.html",
            "http://books.toscrape.com/catalogue/page-2.html",
            "http://books.toscrape.com/catalogue/page-3.html",
            "http://books.toscrape.com/catalogue/page-4.html",
            "http://books.toscrape.com/catalogue/page-5.html",
            "http://books.toscrape.com/catalogue/page-6.html",
            "http://books.toscrape.com/catalogue/page-7.html",
            "http://books.toscrape.com/catalogue/page-8.html",
            "http://books.toscrape.com/catalogue/page-9.html",
            "http://books.toscrape.com/catalogue/page-10.html",

            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1].split(".")[0]
        filename = f"book-{page}.html"
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




