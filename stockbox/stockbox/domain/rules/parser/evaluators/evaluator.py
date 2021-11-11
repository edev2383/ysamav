from .domain_evaluator import DomainEvaluator
from ...parser.token_type import TokenType
from stockbox.stockbox.services.ticker.ticker import Ticker
from ..expr import Expr, Binary, Literal, Unary, Grouping, Domain, DomainBinary


class Evaluator:
    ticker: Ticker

    def __init__(self, ticker: Ticker = None):
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
        left = self.evaluate(binary.left)
        right = self.evaluate(binary.right)
        if binary.operator.type == TokenType.DOMAIN_INDEX:
            return DomainEvaluator(self.ticker).evaluate(binary)
        if binary.operator.type == TokenType.MINUS:
            return float(left) - float(right)
        if binary.operator.type == TokenType.PLUS:
            return self._casePLUS(left, right)
        if binary.operator.type == TokenType.SLASH:
            return float(left) / float(right)
        if binary.operator.type == TokenType.STAR:
            return float(left) * float(right)
        if binary.operator.type == TokenType.GT:
            return float(left) > float(right)
        if binary.operator.type == TokenType.GT_OR_EQ:
            return float(left) >= float(right)
        if binary.operator.type == TokenType.LT:
            return float(left) < float(right)
        if binary.operator.type == TokenType.LT_OR_EQ:
            return float(left) <= float(right)
        if binary.operator.type == TokenType.BANG_EQ:
            return self._is_equal(left, right) == False
        if binary.operator.type == TokenType.EQEQ:
            return self._is_equal(left, right) == True
        return None

    def _eval_literal(self, literal: Literal):
        if literal.token == None:
            return literal.value
        if literal.token.type == TokenType.NUMBER:
            return literal.value
        if literal.token.type == TokenType.STRING:
            return literal.value
        return None

    def _eval_unary(self, unary: Unary):
        right = self.evaluate(unary.right)
        if unary.operator.type == TokenType.MINUS:
            return -float(right)
        if unary.operator.type == TokenType.BANG:
            return self._is_truthy(right) != True
        return None

    def _eval_domain_binary(self, domain_binary: DomainBinary):
        return DomainEvaluator(self.ticker).evaluate(domain_binary)

    def _eval_domain(self, domain: Domain):
        return DomainEvaluator(self.ticker).evaluate(domain)

    def _eval_grouping(self, grouping: Grouping):
        return self.evaluate(grouping.expression)

    def _is_truthy(self, expr: Expr):
        if expr is None:
            return False
        if isinstance(expr, bool):
            return expr
        if type(expr) == str:
            if expr == "":
                return False
        return True

    def _casePLUS(self, left, right):
        if type(left) == float and type(right) == float:
            return float(left) + float(right)
        if type(left) == str and type(right) == str:
            return f"{left}{right}"
        return None

    def _is_equal(self, left, right):
        if left is None and right is None:
            return True
        if left is None:
            return False
        return left == right
