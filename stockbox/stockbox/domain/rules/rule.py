import pandas as pd
from stockbox.stockbox.domain.rules.parser.abs_expr import AbstractExpr
from stockbox.stockbox.domain.rules.parser.evaluators.evaluator import Evaluator
from stockbox.stockbox.domain.rules.rule_result_output import RuleResultOutput
from stockbox.stockbox.domain.rules.rule_statement import RuleStatement
from stockbox.stockbox.domain.ticker.ticker import Ticker
from stockbox.stockbox.common.results.result import Result


class Rule:
    """Accepts a source statement, which is turned into an expression
    (Expr) and then evaluated down to a boolean value. process returns a
    Result object which contains a `status` enum (eSuccess/eFail) and an
    `output` value"""

    expression: AbstractExpr
    ticker: Ticker

    def __init__(self, statement: str):
        rule = RuleStatement(statement)
        self.expression = rule.expression

    def process(self) -> Result:
        """Evaluate the expression returned from the RuleStatement
        process and return the result as a Result object"""
        evaluator = Evaluator(self.ticker)
        evaluate = evaluator.evaluate(self.expression)
        return Result(evaluate, RuleResultOutput(self.expression, evaluator.values))

    def has_ticker(self):
        return self.ticker is not None

    def add_ticker(self, ticker: Ticker):
        self.ticker = ticker
