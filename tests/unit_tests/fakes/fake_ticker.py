from stockbox.stockbox.domain.indicators.indicator_lib import IndicatorLibrary
from .. import ITicker
from .fake_dataframe import fake_history, fake_current


class FakeTicker(ITicker):
    _indicators: IndicatorLibrary

    def __init__(self):
        self._indicators = IndicatorLibrary(self)

    def current(self):
        return fake_current()

    def daily(self):
        return fake_history()

    def weekly(self):
        return fake_history()

    def monthly(self):
        return fake_history()
