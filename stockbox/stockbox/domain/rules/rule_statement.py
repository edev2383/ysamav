from stockbox.stockbox.domain.rules.parser.abs_expr import AbstractExpr
from .parser.evaluators.evaluator import Evaluator
from .parser.statement_scanner import StatementScanner
from .parser.parser import Parser


class RuleStatement:
    """Accepts a statement which is then scanned and passed to the
    parser to return an Expression that can be evaluated"""

    expression: AbstractExpr

    def __init__(self, statement: str):
        self.expression = self._parse_statement(statement)

    def _parse_statement(self, statement: str):
        scanner = StatementScanner(statement)
        return Parser(scanner.scan_tokens()).parse()
