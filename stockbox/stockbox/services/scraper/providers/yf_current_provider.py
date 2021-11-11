from .abs_scraper_provider import AbstractScraperProvider
import requests

class YahooFinanceCurrentProvider(AbstractScraperProvider):
    url: str = "https://finance.yahoo.com/quote/$symbol/history?p=$symbol"

    def _scrape_url(self):
        """ Return the content of the target url """
        res = requests.get(self._template_url(), headers={'User-Agent': 'Mozilla/5.0'})
        if res.status_code != 200:
            raise RuntimeError(f"Error scraping url: {self.url}. Response Code: {res.status_code}")
        return res.content.decode("utf-8")
