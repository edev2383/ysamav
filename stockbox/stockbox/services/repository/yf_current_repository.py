from ..scraper.providers.yf_current_provider_in_params import YahooFinanceCurrentProviderInParams
from ..scraper.providers.yf_current_provider import YahooFinanceCurrentProvider
from ..scraper.parsers.yf_current_parser import YahooFinanceCurrentParser
from ..scraper.scraper import Scraper
from .abs_repository import AbstractRepository

class YahooFinanceCurrentRepository(AbstractRepository):
    pass

    def get(self, args: YahooFinanceCurrentProviderInParams):
        """ returns the current ticker information, based on the in args
            return: YahooFinanceCurrentPayload
        """
        provider = YahooFinanceCurrentProvider(args)
        scraper = Scraper(provider, YahooFinanceCurrentParser())
        self._exec(scraper)
        return scraper.payload
