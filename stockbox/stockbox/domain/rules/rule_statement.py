from stockbox.stockbox.domain.rules.parser.abs_expr import AbstractExpr
from .parser.evaluators.evaluator import Evaluator
from .parser.statement_scanner import StatementScanner
from .parser.parser import Parser


class RuleStatement:
    """Accepts a statement which is then scanned and passed to the
    parser to return an Expression that can be evaluated"""

    expression: AbstractExpr
    scanner: StatementScanner
    parser: Parser
    evaluator: Evaluator
    statement: str

    def __init__(self, statement: str):
        scanner = StatementScanner(statement)
        parser = Parser(scanner.scan_tokens())
        self.expression = parser.parse()
