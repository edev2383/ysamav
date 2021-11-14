from .domain_evaluator import DomainEvaluator
from ...parser.token_type import TokenType
from stockbox.stockbox.services.ticker.ticker import Ticker
from ..expr import Expr, Binary, Literal, Unary, Grouping, Domain, DomainBinary


class Evaluator:
    ticker: Ticker
    values: list

    def __init__(self, ticker: Ticker = None):
        self.ticker = ticker
        self.values = []

    def evaluate(self, expr: Expr):
        if isinstance(expr, Binary):
            binary = self._eval_binary(expr)
            self.values.append(binary)
            return binary
        if isinstance(expr, Literal):
            literal = self._eval_literal(expr)
            self.values.append(literal)
            return literal
        if isinstance(expr, Unary):
            unary = self._eval_unary(expr)
            self.values.append(unary)
            return unary
        if isinstance(expr, Grouping):
            grouping = self._eval_grouping(expr)
            self.values.append(grouping)
            return grouping
        if isinstance(expr, Domain):
            domain = self._eval_domain(expr)
            self.values.append(domain)
            return domain
        if isinstance(expr, DomainBinary):
            domain_binary = self._eval_domain_binary(expr)
            self.values.append(domain_binary)
            return domain_binary

    def _eval_binary(self, binary: Binary):
        left = self.evaluate(binary.left)
        right = self.evaluate(binary.right)
        # print("========================================================")
        # print(f"left: {left}")
        # print(f"right: {right}")
        # print(f"values: {self.values}")
        # print("========================================================")
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
