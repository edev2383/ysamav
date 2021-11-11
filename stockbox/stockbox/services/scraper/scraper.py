from .parsers.abs_scraper_parser import AbstractScraperParser as Parser
from .providers.abs_scraper_provider import AbstractScraperProvider as Provider
from .payload.i_scraper_payload import IScraperPayload
from stockbox.stockbox.services.base.data_provider import DataProvider


class Scraper(DataProvider):
    provider: Provider
    payload: IScraperPayload
    parser: Parser

    def __init__(self, provider: Provider, parser: Parser):
        self.provider = provider
        self.parser = parser

    def scrape(self):
        self.provider.scrape()
        self.payload = self.parser.parse(input=self.provider.output)
