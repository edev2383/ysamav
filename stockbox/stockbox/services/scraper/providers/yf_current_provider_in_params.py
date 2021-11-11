from .i_scraper_provider_in_params import IScraperProviderInParams

class YahooFinanceCurrentProviderInParams(IScraperProviderInParams):
    symbol: str

    def __init__(self, symbol: str):
        self.symbol = symbol
