from abc import ABC, abstractmethod
from stockbox.stockbox.common.helpers.enums import EBucket
from stockbox.stockbox.services.ticker.ticker import Ticker
from stockbox.stockbox.domain.setups.setup import Setup


class IPosition(ABC):
    ticker: Ticker
    setup: Setup
    bucket: EBucket  # this is the target starting state of the stock

    def __init__(self, ticker: Ticker, setup: Setup):
        self.ticker = ticker
        setup.add_ticker(ticker)
        self.setup = setup

    def process(self):
        # temporary return value for testing.
        return self.setup.process(self.bucket)

    def backtest(self):
        ...
