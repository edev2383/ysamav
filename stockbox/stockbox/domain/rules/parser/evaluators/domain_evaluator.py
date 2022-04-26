from stockbox.stockbox.common.helpers.enums import ETickerRequestFrequency
from .dataframe_evaluator import DataFrameEvaluator
from stockbox.stockbox.domain.rules.parser.token_category import TokenCategory
from stockbox.stockbox.domain.rules.parser.token_type import TokenType
from stockbox.stockbox.domain.rules.parser.tv_factory import TVFactory
from stockbox.stockbox.domain.ticker.i_ticker import ITicker
from ..expr import Domain, DomainBinary, Expr, Binary, Literal, Unary, Grouping
import pandas as pd


class DomainEvaluator:
    """Process domain specific evaluations"""

    ticker: ITicker

    interval: ETickerRequestFrequency = ETickerRequestFrequency.eDaily
    index_pointer: int = 0

    dfeval: DataFrameEvaluator = DataFrameEvaluator()

    def __init__(self, ticker: ITicker = None):
        self.ticker = ticker

    def evaluate(self, expr: Expr):
        if isinstance(expr, Binary):
            return self._eval_binary(expr)
        if isinstance(expr, Literal):
            return self._eval_literal(expr)
        if isinstance(expr, Unary):
            return self._eval_unary(expr)
        if isinstance(expr, Grouping):
            return self._eval_grouping(expr)
        if isinstance(expr, Domain):
            return self._eval_domain(expr)
        if isinstance(expr, DomainBinary):
            return self._eval_domain_binary(expr)

    def _eval_binary(self, binary: Binary):
        if binary.operator.type == TokenType.DOMAIN_INDEX:
            self.index_pointer = self.evaluate(binary.left)
            return self.evaluate(binary.right)

    def _eval_unary(self, unary: Unary):
        tv = TVFactory.get(unary.operator.type)
        if tv.category == TokenCategory.INTERVAL:
            self._set_interval(unary.operator.type)
        if unary.operator.type == TokenType.MINUS:
            return -self.evaluate(unary.right)
        return self.evaluate(unary.right)

    def _eval_literal(self, literal: Literal):
        if literal.token != None:
            tv = TVFactory.get(literal.token.type)
            if tv.category == TokenCategory.DOMAIN_KEYWORD:
                idx = self.index_pointer
                col = literal.value
                return self.dfeval.evaluate(self._resolve_df(), idx, col)
        return literal.value

    def _eval_grouping(self, grouping: Grouping):
        return None

    def _eval_domain(self, domain: Domain):
        if domain.category == TokenCategory.DOMAIN_KEYWORD:
            idx = self.index_pointer
            col = domain.column
            return self.dfeval.evaluate(self._resolve_df(), idx, col)
        if domain.category == TokenCategory.INDICATOR:
            idx = self.index_pointer
            col = domain.column
            self.ticker.load_indicator(col, self.interval)
            return self.dfeval.evaluate(self._resolve_df(), idx, col)

    def _resolve_df(self):
        if self.ticker is None:
            raise ValueError("Domain Evaluator: Ticker value missing")
        return self.ticker.clone_for_setup(self.interval)

    def _eval_domain_binary(self, domain_binary: DomainBinary):
        if domain_binary.operator.type == TokenType.DOMAIN_INDEX:
            self.index_pointer = self.evaluate(domain_binary.left)
            return self.evaluate(domain_binary.right)

    def _set_interval(self, interval_token: TokenType):
        if interval_token == TokenType.DAILY:
            self.interval = ETickerRequestFrequency.eDaily
        if interval_token == TokenType.WEEKLY:
            self.interval = ETickerRequestFrequency.eWeekly
        if interval_token == TokenType.MONTHLY:
            self.interval = ETickerRequestFrequency.eMonthly
