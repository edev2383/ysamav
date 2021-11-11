from stockbox.stockbox.common.helpers.enums import ETickerRequestFrequency
from .i_scraper_provider_in_params import IScraperProviderInParams


class YahooFinanceHistoryProviderInParams(IScraperProviderInParams):
    symbol: str
    date_start_str: str
    date_end_str: str
    date_start_int: int
    date_end_int: int
    frequency: str # d,w,m

    def __init__(self, symbol: str,
        frequency: ETickerRequestFrequency,
        date_start_str: str = None,
        date_end_str: str = None,
        date_start_int: int = None,
        date_end_int: int = None
    ):
        self.symbol = symbol
        self.frequency = frequency.value
        self.date_start_str = date_start_str
        self.date_end_str = date_end_str
        self.date_end_int = date_end_int
        self.date_start_int = date_start_int
