from stockbox.stockbox.common.helpers.enums import ETickerRequestFrequency
from stockbox.stockbox.domain.indicators.indicator_factory import IndicatorFactory
from stockbox.stockbox.domain.indicators.sma import SimpleMovingAverage
from stockbox.stockbox.domain.indicators.indicator_lib import IndicatorLibrary
from . import Ticker


def test_simple_moving_average_indicator():
    EXPECTED_TAG = "SMA(14)"
    ticker_one = Ticker("MSFT")
    indicator = IndicatorFactory().create(EXPECTED_TAG, ticker_one.daily().dataframe)
    assert isinstance(indicator, SimpleMovingAverage)
    assert indicator.output.empty == False
    assert indicator.df_colkey == EXPECTED_TAG


def test_daily_ticker_loads_with_expected_default_indicators():
    EXPECTED_TAGS = ["SMA(10)", "SMA(50)", "SMA(200)"]
    ticker = Ticker("MSFT")
    ticker.daily()
    assert isinstance(ticker._indicators, IndicatorLibrary)
    daily_inds = ticker._indicators.get(ETickerRequestFrequency.eDaily)
    assert len(daily_inds) == len(EXPECTED_TAGS)
    for ind in daily_inds:
        assert ind.df_colkey in EXPECTED_TAGS


def test_weekly_ticker_loads_with_expected_default_indicators():
    EXPECTED_TAGS = ["SMA(10)", "SMA(50)", "SMA(200)"]
    ticker = Ticker("MSFT")
    ticker.weekly()
    assert isinstance(ticker._indicators, IndicatorLibrary)
    weekly_inds = ticker._indicators.get(ETickerRequestFrequency.eWeekly)
    assert len(weekly_inds) == len(EXPECTED_TAGS)
    for ind in weekly_inds:
        assert ind.df_colkey in EXPECTED_TAGS


def test_monthly_ticker_loads_with_expected_default_indicators():
    EXPECTED_TAGS = ["SMA(10)", "SMA(50)", "SMA(200)"]
    ticker = Ticker("MSFT")
    ticker.monthly()
    assert isinstance(ticker._indicators, IndicatorLibrary)
    monthly_inds = ticker._indicators.get(ETickerRequestFrequency.eMonthly)
    assert len(monthly_inds) == len(EXPECTED_TAGS)
    for ind in monthly_inds:
        assert ind.df_colkey in EXPECTED_TAGS
