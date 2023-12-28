
import requests
from bs4 import BeautifulSoup 
import mechanize

# url = "https://sarallagani.com/investment-opportunity"


url = 'https://sarallagani.com/investment-opportunity'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
def Fetch():
    res = requests.get(url, headers=headers)
    return res
# html = Fetch().text
# soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify)
print(Fetch().text)