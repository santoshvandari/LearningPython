# Scraping Dynamic Javascript Websites with Scrapy and Scrapy-playwright

The world of web scraping is truly fascinating. Automating data collection from website is both fun and a useful skill.

Scrapy is a popular Python package that makes scraping website a breeze. However, it works best on static pages. In case of Javascript-heavy websites that load data on-demand or require rendering and user input Scrapy struggles a lot.

In this article I will explore ways to use Scrapy to scrape dynamic websites.



This article will rely heavily on videos by John Watson Rooney. Check out his Youtube channel because he has a lot of amazing video on web scraping!

Let's begin. We will explore scraping of dynamic website using scrapy-playwright.



Note: I use `example.com `as an example. I don't want to use existing website and inadvertently ddos it. Scraping should be done responsibly and we should always read website's ToS to see if they even allow scraping. This article for educational purposes only.



First we will create our virtual environment and install `scrapy`, `scrapy-playwright`, and initialize playwright:
```
$ python -m virtualenv venv
$ source venv/bin/activate
$ pip install scrapy scrapy-playwright
$ playwright install
```


We need a scrapy project to proceed. Luckily, scrapy has a built-in command to create a new project. Let's create a scrapy project and change into the newly created folder:
```
$ scrapy startproject playwright_demo
$ cd playwright_demo
```


Next we will create a new spider.

```
$ scrapy genspider pwspider example.com
# Output
Created spider 'pwspider' using template 'basic' in module:
  playwright_demo.spiders.pwspider
```


You should see a new folder in your working directory named playwright_demo with similar structure (you may have different numbers next to python depending on your version):

```
├── playwright_demo
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   └── settings.cpython-38.pyc
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders
│       ├── __init__.py
│       ├── __pycache__
│       │   └── __init__.cpython-38.pyc
│       └── pwspider.py
└── scrapy.cfg

4 directories, 11 files
```


Now we need to modify scrapy's settings to allow it to work with playwright. Instructions can be found on playwright's GitHub page. We need to add settings for `DOWNLOAD_HANDLERS` and `TWISTED_REACTOR`. New settings that were added can be found between `###`.
This is what the settings file should look like:

```
# playwright_demo/settings.py

# Scrapy settings for playwright_demo project
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'playwright_demo'

SPIDER_MODULES = ['playwright_demo.spiders']
NEWSPIDER_MODULE = 'playwright_demo.spiders'

### Playwright settings
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
###


# More scrapy settings down below...

```

Another thing we need to edit is the spider itself. We need to add a `start_requests()` method and delete a couple of lines from the spider. Here is the file:

```
# playwright_demo/spiders/pwspider.py

import scrapy


class PwspiderSpider(scrapy.Spider):
    name = 'pwspider'

    def start_requests(self):
        yield scrapy.Request('example.com', meta={'playwright': True})

    def parse(self, response):
        yield {
            'text': response.text,
        }
```

Ok, we got the basic setup. Now we need to inspect the source of the website we want to scrape.
We are looking for something similar to this:
```
We're sorry, but the site doesn't work properly without Javascript enabled.
```


What this means is that we have to actually load the website and allow it to load the data we want to scrape.

If we try to run our spider with this command and output the result of the scrape into the o`utput_data.json` we will get data back:

```
scrapy crawl pwspider -o output_data.json
```


The problem is that we get junk data. Scrapy does not give the website enough time to load the data we want.

What we do is go to the website you want to scrape and start looking for selectors, ids, and classes of items we want. We need to tell playwright to wait until the data we want is loaded and only after that scrape it.



We will change the `meta` dictionary inside the `start_requests` method to point scrapy and playwright in the right direction. I will use imaginary `div` that has an id `itemName`. For the price, it is an imaginary `div` `form-group` that contains a `label` with price. There should also be an `async` in front of the `parse` method or it will not work. Here is the updated spider file:

```
# playwright_demo/spiders/pwspider.py

import scrapy
from scrapy_playwright.page import PageCoroutine


class PwspiderSpider(scrapy.Spider):
    name = 'pwspider'

    def start_requests(self):
        yield scrapy.Request('https://twitter.com',
                             meta=dict(
                                 playwright=True,
                                 playwright_include_page=True,
                                 playwright_page_coroutines=[
                                     # This where we can implement scrolling if we want
                                     PageCoroutine(
                                         'wait_for_selector', 'div#itemName')
                                 ]
                             )
                             )

    async def parse(self, response):
        for item in response.css('div.card'):
            yield {
                'name': item.css('h3::text').get(),
                'price': item.css('div.form-group label::text').get()
            }
```


If we run our spider again:
```
scrapy crawl pwspider -o output_data.json
```


Our output file will have something similar to this output:

```
// output_data.json

[
    {"name": "Item1", "price": "$14.99"}
    {"name": "Item2", "price": "$19.99"}
    {"name": "Item3", "price": "$134.99"}
    {"name": "Item4", "price": "$17.99"}
]
```


This is it. Now you know how to scrape dynamic websites.