import pandas as pd
from stockbox.stockbox.domain.rules.parse_statement import ParseStatement
from stockbox.stockbox.domain.rules.parser.abs_expr import AbstractExpr
from stockbox.stockbox.domain.rules.parser.evaluators.evaluator import Evaluator
from stockbox.stockbox.domain.rules.rule_statement import RuleStatement
from stockbox.stockbox.services.ticker.ticker import Ticker
from stockbox.stockbox.common.results.result import Result


class Rule:
    expression: AbstractExpr
    ticker: Ticker
    statement: str

    def __init__(self, statement: str):
        rule = RuleStatement(statement)
        self.statement = statement
        self.expression = rule.expression

    def process(self) -> Result:
        """Evaluate the expression returned from the RuleStatement
        process and return the result as a Result object"""
        evaluate = Evaluator(self.ticker).evaluate(self.expression)
        return Result(evaluate, self.expression)

    def has_ticker(self):
        return self.ticker is not None

    def add_ticker(self, ticker: Ticker):
        self.ticker = ticker
