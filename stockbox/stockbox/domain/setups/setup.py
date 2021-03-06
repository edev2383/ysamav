from stockbox.stockbox.common.helpers.enums import EBucket
from stockbox.stockbox.domain.actions.i_action import IAction
from stockbox.stockbox.domain.rules.ruleset import RuleSet
from stockbox.stockbox.domain.rules.ruleset_list import RuleSetList
from stockbox.stockbox.domain.ticker.ticker import Ticker
from stockbox.stockbox.common.results.result import ResultList


class Setup:
    ticker: Ticker
    rulesets: RuleSetList

    def __init__(self, ticker: Ticker = None):
        self.ticker = ticker
        self.rulesets = RuleSetList()

    def process(self, bucket: EBucket) -> ResultList:
        ruleset = self.find_ruleset(bucket)
        if ruleset.has_ticker() == False:
            """Add the ticker if the RuleSet is missing the property"""
            ruleset.add_ticker(self.ticker)
        return ruleset.process()

    def has_ticker(self):
        return self.ticker != None

    def add_ticker(self, ticker: Ticker):
        self.ticker = ticker

    def add_ruleset(self, ruleset: RuleSet):
        ruleset.add_ticker(self.ticker)
        self.rulesets.append(ruleset)

    def find_ruleset(self, bucket: EBucket) -> RuleSet:
        return self.rulesets.find(bucket)

    def get_action(self, bucket: EBucket) -> IAction:
        ruleset = self.find_ruleset(bucket)
        if ruleset is None:
            raise ValueError("RuleSet not found")
        return ruleset.get_action()
