from stockbox.stockbox.common.helpers.enums import EBucket
from stockbox.stockbox.services.ticker.ticker import Ticker


class IAction:
    to_bucket: EBucket

    def transition(self, ticker: Ticker):
        ...
