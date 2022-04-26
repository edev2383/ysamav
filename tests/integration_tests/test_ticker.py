from stockbox.stockbox.services.scraper.providers.yf_current_provider_in_params import (
    YahooFinanceCurrentProviderInParams,
)
from . import Ticker
from . import YahooFinanceCurrentPayload
import pandas as pd


def test_ticker_current_return_value_is_correct():
    output = Ticker("TSLA").current()
    # output is of the correct type
    assert isinstance(output, YahooFinanceCurrentPayload)
    # the payload properties are of the expected type
    assert type(output.date) == str
    assert type(output.open) == float
    assert type(output.high) == float
    assert type(output.low) == float
    assert type(output.close) == float
    assert type(output.adjclose) == float
    assert type(output.volume) == int
    # the values are *generally* correct
    assert output.low <= output.high
    assert output.low <= output.close or output.low <= output.open
    assert output.high >= output.close or output.high >= output.open


def test_ticker_history_daily_return_value_is_correct():
    output = Ticker("MSFT").daily()
    # payload has a value
    assert output != None
    # payload is the correct type/instance
    assert isinstance(output.dataframe, pd.DataFrame)
    # payload is expected length (eOneYear is default)
    assert output.dataframe.empty != True
    # trading days vary between 250-253, confirm it, account for header
    assert len(output.dataframe.index) >= 250
    assert len(output.dataframe.index) <= 254
    # print(output.dataframe.head())


def test_ticker_history_weekly_return_value_is_correct():
    output = Ticker("MSFT").weekly()
    # payload has a value
    assert output != None
    # payload is the correct type/instance
    assert isinstance(output.dataframe, pd.DataFrame)
    # payload is expected length (eOneYear is default)
    assert output.dataframe.empty != True
    # accounting for varience 51-53 trading rows in dataframe
    assert len(output.dataframe.index) >= 51
    assert len(output.dataframe.index) <= 54
    # print(output.dataframe.head())


def test_ticker_history_monthly_return_value_is_correct():
    output = Ticker("MSFT").monthly()
    # payload has a value
    assert output != None
    # payload is the correct type/instance
    assert isinstance(output.dataframe, pd.DataFrame)
    # payload is expected length (eOneYear is default)
    assert output.dataframe.empty != True
    assert len(output.dataframe.index) >= 12
    assert len(output.dataframe.index) <= 14

    # print(output.dataframe.head())
