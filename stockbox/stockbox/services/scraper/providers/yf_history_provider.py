from .abs_scraper_provider import AbstractScraperProvider
import requests


class YahooFinanceHistoryProvider(AbstractScraperProvider):
    url: str = "https://query1.finance.yahoo.com/v7/finance/download/$symbol?period1=$date_start_int&period2=$date_end_int&interval=$frequency&events=history&includeAdjustedClose=true"

    def _scrape_url(self):
        """ Return the content of the target url """
        res = requests.get(self._template_url(), headers={'User-Agent': 'Mozilla/5.0'})
        if res.status_code != 200:
            raise RuntimeError(f"Error scraping url: {self.url}. Response Code: {res.status_code}")
        return res.text
