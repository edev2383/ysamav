from stockbox.stockbox.common.helpers.enums import EBucket
from stockbox.stockbox.domain.setups.setup import Setup
from stockbox.stockbox.services.ticker.ticker import Ticker


class PositionModel:
    ticker: Ticker
    setup: Setup
    bucket: EBucket

    def __init__(self, ticker: Ticker, setup: Setup, bucket: EBucket):
        self.ticker = ticker
        setup.add_ticker(ticker)
        self.setup = setup
        self.bucket = bucket
