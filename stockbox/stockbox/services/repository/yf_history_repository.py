from .abs_repository import AbstractRepository
from ..scraper.providers.yf_history_provider_in_params import YahooFinanceHistoryProviderInParams
from ..scraper.providers.yf_history_provider import YahooFinanceHistoryProvider
from ..scraper.parsers.yf_history_parser import YahooFinanceHistoryParser
from ..scraper.scraper import Scraper

class YahooFinanceHistoryRepository(AbstractRepository):

    def get(self, args: YahooFinanceHistoryProviderInParams):
        """ returns historical ticker dataframe
            return: YahooFinanceHistoryPayload
        """
        provider = YahooFinanceHistoryProvider(args)
        scraper = Scraper(provider, YahooFinanceHistoryParser())
        self._exec(scraper)
        return scraper.payload