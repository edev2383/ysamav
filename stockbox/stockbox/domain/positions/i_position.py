from abc import ABC, abstractmethod
from stockbox.stockbox.common.helpers.enums import EBucket
from stockbox.stockbox.common.results.result import ResultList
from stockbox.stockbox.domain.actions.i_action import IAction
from stockbox.stockbox.domain.positions.position_model import PositionModel
from stockbox.stockbox.services.ticker.ticker import Ticker
from stockbox.stockbox.domain.setups.setup import Setup


class IPosition(ABC):
    """The Position class is responsible for running the setups against
    the provided ticker and returning the action from the RuleSet upon
    success"""

    ticker: Ticker
    setup: Setup
    # this is the target starting state of the stock
    bucket: EBucket
    # on a successful run_setup, action gets raised from RuleSet
    action: IAction
    # run_setup returns a ResultList
    results: ResultList

    def __init__(self, model: PositionModel):
        self.ticker = model.ticker
        self.setup = model.setup
        self.bucket = model.bucket

    def process(self):
        self.results = self.run_setup()
        if self.results.has_errors() == False:
            self.action = self.get_action()

    def run_setup(self) -> ResultList:
        if self.setup.has_ticker() == False:
            self.setup.add_ticker(self.ticker)
        return self.setup.process(self.bucket)

    def get_action(self) -> IAction:
        return self.setup.get_action(self.bucket)

    def backtest(self):
        ...
