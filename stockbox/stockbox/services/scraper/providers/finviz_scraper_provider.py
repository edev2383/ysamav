from .abs_scraper_provider import AbstractScraperProvider


class FinVizScraperProvider(AbstractScraperProvider):
    url: str = "FINVIZ"

    def _scrape_url(self):
        return self.url
