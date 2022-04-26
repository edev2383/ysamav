from collections import namedtuple
from stockbox.stockbox.common.helpers.enums import ETickerRequestFrequency
from stockbox.stockbox.domain.indicators.indicator_factory import IndicatorFactory
from .indicator_collection import IndicatorCollection


class IndicatorLibrary:
    """ The IndicatorLibray is a contained repository of indicators within the 
    Ticker class."""
    daily: IndicatorCollection()
    weekly: IndicatorCollection()
    monthly: IndicatorCollection()
    factory = IndicatorFactory()

    def __init__(self, ticker):
        self.ticker = ticker
        self.daily = IndicatorCollection()
        self.weekly = IndicatorCollection()
        self.monthly = IndicatorCollection()

    def exists(self, key: str, frequency: ETickerRequestFrequency):
        collection = self.parse_target(frequency).col
        return collection.exists(key)

    def add(self, key: str, frequency: ETickerRequestFrequency):
        # get the requested target collection and dataframe
        target = self.parse_target(frequency)
        # create the indicator
        indicator = self.factory.create(key, target.data.dataframe.copy())
        # append the indicator to the requested collection
        target.col.append(indicator)

    def get(self, frequency: ETickerRequestFrequency):
        """returns the requested IndicatorCollection object"""
        target = self.parse_target(frequency)
        return target.col

    def parse_target(self, frequency: ETickerRequestFrequency):
        """returns a tuple of the indicator collection and the
        appropriate ticker df"""
        Out = namedtuple("Out", "col data")
        if frequency is ETickerRequestFrequency.eDaily:
            return Out(self.daily, self.ticker.daily())
        if frequency is ETickerRequestFrequency.eWeekly:
            return Out(self.weekly, self.ticker.weekly())
        if frequency is ETickerRequestFrequency.eMonthly:
            return Out(self.monthly, self.ticker.monthly())
