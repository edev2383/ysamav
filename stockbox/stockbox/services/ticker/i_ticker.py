from stockbox.stockbox.common.helpers.enums import (
    EBucket,
    ETickerRequestFrequency,
    ETickerRequestRange,
)
from stockbox.stockbox.services.indicators.abs_indicator import AbstractIndicator
from stockbox.stockbox.services.indicators.indicator_factory import IndicatorFactory
from stockbox.stockbox.services.repository.yf_current_repository import (
    YahooFinanceCurrentRepository,
)
from stockbox.stockbox.services.repository.yf_history_repository import (
    YahooFinanceHistoryRepository,
)
from stockbox.stockbox.services.scraper.payload.i_scraper_payload import IScraperPayload
from stockbox.stockbox.services.scraper.providers.yf_current_provider_in_params import (
    YahooFinanceCurrentProviderInParams,
)
from stockbox.stockbox.services.scraper.providers.yf_history_provider_in_params import (
    YahooFinanceHistoryProviderInParams,
)
from stockbox.stockbox.services.ticker.indicator_collection import IndicatorCollection
from stockbox.stockbox.services.ticker.indicator_lib import IndicatorLibrary
from ..scraper.payload.yf_history_payload import YahooFinanceHistoryPayload
from ..scraper.payload.yf_current_payload import YahooFinanceCurrentPayload
from stockbox.stockbox.common.helpers.date_range import DateRange
import pandas as pd


class ITicker:
    symbol: str
    range: DateRange
    # holders for scraped content
    _current: YahooFinanceCurrentPayload = None
    _daily: YahooFinanceHistoryPayload = None
    _weekly: YahooFinanceHistoryPayload = None
    _monthly: YahooFinanceHistoryPayload = None
    # a container class for all created indicators
    _indicators: IndicatorLibrary
    _default_range: ETickerRequestRange = ETickerRequestRange.eOneYear

    def __init__(self, symbol: str, range: ETickerRequestRange = None):
        self.symbol = symbol
        self.range = self._set_range(range)
        self._indicators = IndicatorLibrary(self)

    def current(self):
        if self._current is None:
            self._current = self._get_current_data()
        return self._current

    def daily(self):
        if self._daily is None:
            self._daily = self._get_daily_data()
            self._add_default_indicators(ETickerRequestFrequency.eDaily)
        return self._daily

    def weekly(self):
        if self._weekly is None:
            self._weekly = self._get_weekly_data()
            self._add_default_indicators(ETickerRequestFrequency.eWeekly)
        return self._weekly

    def monthly(self):
        if self._monthly is None:
            self._monthly = self._get_monthly_data()
            self._add_default_indicators(ETickerRequestFrequency.eMonthly)
        return self._monthly

    def clone_for_setup(self, frequency: ETickerRequestFrequency):
        """clone the Ticker's dataframe and merge with existing
        indicators"""
        targeted_payload = self._get_payload(frequency)
        __df = targeted_payload.dataframe.copy()
        __ic = self._indicators.get(frequency)
        self._merge_indicators(__df, __ic)
        return __df

    def load_indicator(self, indicator_key: str, interval: ETickerRequestFrequency):
        if self._indicators.exists(indicator_key, interval) == False:
            self._add_indicator(indicator_key, interval)

    def _get_current_data(self):
        repo = YahooFinanceCurrentRepository()
        return repo.get(YahooFinanceCurrentProviderInParams(self.symbol))

    def _get_daily_data(self):
        repo = YahooFinanceHistoryRepository()
        scraped_data = repo.get(
            YahooFinanceHistoryProviderInParams(
                symbol=self.symbol,
                frequency=ETickerRequestFrequency.eDaily,
                date_start_int=self.range.range_int["start"],
                date_end_int=self.range.range_int["end"],
            )
        )
        return scraped_data

    def _get_weekly_data(self):
        repo = YahooFinanceHistoryRepository()
        scraped_data = repo.get(
            YahooFinanceHistoryProviderInParams(
                symbol=self.symbol,
                frequency=ETickerRequestFrequency.eWeekly,
                date_start_int=self.range.range_int["start"],
                date_end_int=self.range.range_int["end"],
            )
        )
        return scraped_data

    def _get_monthly_data(self):
        repo = YahooFinanceHistoryRepository()
        scraped_data = repo.get(
            YahooFinanceHistoryProviderInParams(
                symbol=self.symbol,
                frequency=ETickerRequestFrequency.eMonthly,
                date_start_int=self.range.range_int["start"],
                date_end_int=self.range.range_int["end"],
            )
        )
        return scraped_data

    def _add_default_indicators(self, frequency: ETickerRequestFrequency):
        self._add_indicator("SMA(10)", frequency)
        self._add_indicator("SMA(50)", frequency)
        self._add_indicator("SMA(200)", frequency)

    def _add_indicator(self, key: str, frequency: ETickerRequestFrequency):
        self._indicators.add(key, frequency)

    def _merge_indicators(self, df: pd.DataFrame, ind_col: IndicatorCollection):
        """for all indicators in the given indicator collection, add
        the indicator to the dataframe. This allows the indicators to
        have more encapsulated control, only merging them with the
        dataframe when necessary"""
        for ind in ind_col:
            self._merge_inidcator(df, ind)

    def _merge_inidcator(self, df: pd.DataFrame, ind: AbstractIndicator):
        df[ind.df_colkey] = ind.output

    def _get_payload(self, frequency: ETickerRequestFrequency):
        if frequency is ETickerRequestFrequency.eDaily:
            return self.daily()
        if frequency is ETickerRequestFrequency.eWeekly:
            return self.weekly()
        if frequency is ETickerRequestFrequency.eMonthly:
            return self.monthly()

    def _set_range(self, range: ETickerRequestRange = None):
        if range == None:
            range = self._default_range
        return DateRange(range)
