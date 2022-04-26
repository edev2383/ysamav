from stockbox.stockbox.common.helpers.enums import EBucket
from stockbox.stockbox.domain.actions.i_action import IAction
from stockbox.stockbox.domain.ticker.ticker import Ticker
from stockbox.stockbox.common.results.result import ResultList
from .rule_list import RuleList
from .rule import Rule


class RuleSet:
    """RuleSet describes some behavior and state for a given set of
    Rules. A RuleSet will also define the action to be taken and the
    target bucket, to which this collection of rules belong.

    A PositionController will have a bucket state along with its own
    Ticker and Setup objects. The PC will call the Setup and know which
    RuleSet to target through its EBucket value"""

    rules: RuleList
    ticker: Ticker
    results: ResultList
    action: IAction
    bucket: EBucket

    def __init__(
        self, ticker: Ticker = None, action: IAction = None, bucket: EBucket = None
    ):
        self.rules = RuleList()
        self.results = ResultList()
        self.ticker = ticker
        self.action = action

    def process(self) -> ResultList:
        """Loop through the rules contained within the RuleSet and add
        each Result to the ResultList response obj. This ResultList will
        be passed up to the Setup and then the PositionController which
        will decide what to do from there"""
        for rule in self.rules:
            if rule.has_ticker() == False:
                rule.add_ticker(self.ticker)
            self.results.append(rule.process())
        return self.results

    def has_ticker(self):
        return self.ticker is not None

    def get_action(self) -> IAction:
        return self.action

    def set_bucket(self, bucket: EBucket):
        self.bucket = bucket

    def add_rule(self, rule: Rule):
        rule.add_ticker(self.ticker)
        self.rules.append(rule)

    def add_action(self, action: IAction):
        self.action = action

    def add_ticker(self, ticker: Ticker):
        self.ticker = ticker
