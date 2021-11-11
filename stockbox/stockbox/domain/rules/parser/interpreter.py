from stockbox.stockbox.domain.rules.parser.abs_expr import AbstractExpr, ExprVisitor
from stockbox.stockbox.domain.rules.parser.evaluators.evaluator import Evaluator
from stockbox.stockbox.domain.rules.parser.token_category import TokenCategory
from stockbox.stockbox.services.ticker.ticker import Ticker
from .expr import Expr, Literal, Grouping, Unary, Binary


class Interpreter(ExprVisitor):
    ticker: Ticker

    def __init__(self, ticker: Ticker = None):
        self.ticker = ticker

    def visit(self, expr: Expr):
        return Evaluator(self.ticker).evaluate(expr)

    def visitLiteral(self, literal: Literal):
        return Evaluator(self.ticker).evaluate(literal)

    def visitBinary(self, binary: Binary):
        return Evaluator(self.ticker).evaluate(binary)

    def visitGrouping(self, grouping: Grouping):
        return Evaluator(self.ticker).evaluate(grouping)

    def visitUnary(self, unary: Unary):
        return Evaluator(self.ticker).evaluate(unary)

    def _evaluate(self, expr: AbstractExpr):
        return Evaluator(self.ticker).evaluate(expr)
