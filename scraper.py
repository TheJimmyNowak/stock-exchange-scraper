import requests
import urllib
from bs4 import BeautifulSoup


class FinanceScraper:
    def __init__(self):
        self.USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        self.GOOGLE_URL = "https://www.google.com/search?tbm=fin&q="
        
    def get_intraday(self, symbol: str) -> list:
        symbol = urllib.parse.quote(symbol)
        url = self.GOOGLE_URL + symbol
        response = requests.get(url, headers=self.USER_AGENT)
        soup = BeautifulSoup(response.text, 'html.parser')

        scraps = [0,0,0]

        for tag in soup.find_all('td', class_="iyjjgb"):
            tag = tag.text.replace('\xa0', '')
            tag = float(tag.replace(',', '.'))
            scraps[i] = tag
            
        return scraps
    
