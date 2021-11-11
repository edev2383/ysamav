from . import YahooFinanceCurrentProvider, YahooFinanceCurrentProviderInParams
from . import ETickerRequestFrequency, ETickerRequestRange, DateRange
from . import YahooFinanceHistoryProvider, YahooFinanceHistoryProviderInParams


def test_current_provider_scrape_returns_value():
    provider_in_params = YahooFinanceCurrentProviderInParams("MSFT")
    provider = YahooFinanceCurrentProvider(provider_in_params)
    provider.scrape()
    assert provider.output != None

def test_history_provider_scrape_returns_value():
    dr = DateRange(ETickerRequestRange.eOneYear)
    in_param = YahooFinanceHistoryProviderInParams(
        symbol="MSFT", 
        frequency=ETickerRequestFrequency.eDaily, 
        date_start_int=dr.range_int["start"], 
        date_end_int=dr.range_int["end"])
    provider = YahooFinanceHistoryProvider(in_param)
    provider.scrape()
    assert provider.output != None
