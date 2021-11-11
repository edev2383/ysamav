from .i_scraper_payload import IScraperPayload

class YahooFinanceCurrentPayload(IScraperPayload):
    date: str
    open: float
    high: float
    low: float
    close: float
    adjclose: float
    volume: int