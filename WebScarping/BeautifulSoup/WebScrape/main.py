import requests
from bs4 import BeautifulSoup 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
import time 

url = "https://sarallagani.com/investment-opportunity"

# Create ChromeOptions
# options = webdriver.ChromeOptions()
# Add any additional options you need, e.g., headless mode
# options.add_argument('--headless')

# Specify the path to ChromeDriver
driver_path = '/home/wabisabi/Desktop/WebScrape/chromedriver'
options = Options()
options.add_argument('--binary-location={}'.format(driver_path))


# Create the webdriver instance
driver = webdriver.Chrome(options=options)
driver.get(url) 

time.sleep(5)  # Use sleep to give the page some time to load

html = driver.page_source 
soup = BeautifulSoup(html, "html.parser")
print(soup.prettify()) 

driver.quit()  # Use quit() to properly close the webdriver

