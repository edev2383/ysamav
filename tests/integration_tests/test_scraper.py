from stockbox.stockbox.common.helpers.date_range import DateRange
from stockbox.stockbox.common.helpers.enums import (
    ETickerRequestFrequency,
    ETickerRequestRange,
)
from stockbox.stockbox.services.scraper.parsers.yf_current_parser import (
    YahooFinanceCurrentParser,
)
from stockbox.stockbox.services.scraper.parsers.yf_history_parser import (
    YahooFinanceHistoryParser,
)
from stockbox.stockbox.services.scraper.payload.i_scraper_payload import IScraperPayload
from stockbox.stockbox.services.scraper.providers.yf_current_provider import (
    YahooFinanceCurrentProvider,
)
from stockbox.stockbox.services.scraper.providers.yf_current_provider_in_params import (
    YahooFinanceCurrentProviderInParams,
)
from stockbox.stockbox.services.scraper.providers.yf_history_provider import (
    YahooFinanceHistoryProvider,
)
from stockbox.stockbox.services.scraper.providers.yf_history_provider_in_params import (
    YahooFinanceHistoryProviderInParams,
)
from stockbox.stockbox.services.scraper.scraper import Scraper
import pandas as pd


def test_yf_current_returns_expected_output():
    """These tests are similar to tests in test_ticker.py, but is
    testing this behavior outside of the Ticker class"""
    in_params = YahooFinanceCurrentProviderInParams("MSFT")
    provider = YahooFinanceCurrentProvider(in_params)
    parser = YahooFinanceCurrentParser()
    scraper = Scraper(provider, parser)
    scraper.scrape()
    # payload has a value
    assert scraper.payload != None
    # payload is the correct type/instance
    assert isinstance(scraper.payload, IScraperPayload)
    # the payload properties are of the expected type
    assert type(scraper.payload.date) == str
    assert type(scraper.payload.open) == float
    assert type(scraper.payload.high) == float
    assert type(scraper.payload.low) == float
    assert type(scraper.payload.close) == float
    assert type(scraper.payload.adjclose) == float
    assert type(scraper.payload.volume) == int
    # the values are *generally* correct
    assert scraper.payload.low <= scraper.payload.high
    assert (
        scraper.payload.low <= scraper.payload.close
        or scraper.payload.low <= scraper.payload.open
    )
    assert (
        scraper.payload.high >= scraper.payload.close
        or scraper.payload.high >= scraper.payload.open
    )


def test_yf_daily_history_returns_expected_output():
    """These tests are similar to tests in test_ticker.py, but is
    testing this behavior outside of the Ticker class"""
    dr = DateRange(ETickerRequestRange.eOneYear)
    in_params = YahooFinanceHistoryProviderInParams(
        symbol="MSFT",
        frequency=ETickerRequestFrequency.eDaily,
        date_start_int=dr.range_int["start"],
        date_end_int=dr.range_int["end"],
    )
    provider = YahooFinanceHistoryProvider(in_params)
    parser = YahooFinanceHistoryParser()
    scraper = Scraper(provider, parser)
    scraper.scrape()
    # payload has a value
    assert scraper.payload != None
    # payload is the correct type/instance
    assert isinstance(scraper.payload.dataframe, pd.DataFrame)
    # payload is expected length (eOneYear)
    assert scraper.payload.dataframe.empty != True
    assert len(scraper.payload.dataframe.index) >= 250
    assert len(scraper.payload.dataframe.index) <= 254


def test_yf_weekly_history_returns_expected_output():
    """These tests are similar to tests in test_ticker.py, but is
    testing this behavior outside of the Ticker class"""
    dr = DateRange(ETickerRequestRange.eOneYear)
    in_params = YahooFinanceHistoryProviderInParams(
        symbol="MSFT",
        frequency=ETickerRequestFrequency.eWeekly,
        date_start_int=dr.range_int["start"],
        date_end_int=dr.range_int["end"],
    )
    provider = YahooFinanceHistoryProvider(in_params)
    parser = YahooFinanceHistoryParser()
    scraper = Scraper(provider, parser)
    scraper.scrape()
    # payload has a value
    assert scraper.payload != None
    # payload is the correct type/instance
    assert isinstance(scraper.payload.dataframe, pd.DataFrame)
    # payload is expected length (eOneYear)
    assert scraper.payload.dataframe.empty != True
    assert len(scraper.payload.dataframe.index) >= 51
    assert len(scraper.payload.dataframe.index) <= 54


def test_yf_monthly_history_returns_expected_output():
    """These tests are similar to tests in test_ticker.py, but is
    testing this behavior outside of the Ticker class"""
    dr = DateRange(ETickerRequestRange.eOneYear)
    in_params = YahooFinanceHistoryProviderInParams(
        symbol="MSFT",
        frequency=ETickerRequestFrequency.eMonthly,
        date_start_int=dr.range_int["start"],
        date_end_int=dr.range_int["end"],
    )
    provider = YahooFinanceHistoryProvider(in_params)
    parser = YahooFinanceHistoryParser()
    scraper = Scraper(provider, parser)
    scraper.scrape()
    # payload has a value
    assert scraper.payload != None
    # payload is the correct type/instance
    assert isinstance(scraper.payload.dataframe, pd.DataFrame)
    # payload is expected length (eOneYear)
    assert scraper.payload.dataframe.empty != True
    assert len(scraper.payload.dataframe.index) >= 12
    assert len(scraper.payload.dataframe.index) <= 14
