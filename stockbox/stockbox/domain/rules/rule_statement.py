from stockbox.stockbox.domain.rules.parser.abs_expr import AbstractExpr
from .parser.evaluators.evaluator import Evaluator
from .parser.statement_scanner import StatementScanner
from .parser.parser import Parser
from .parser.interpreter import Interpreter


class RuleStatement:
    expression: AbstractExpr
    scanner: StatementScanner
    parser: Parser
    interpreter: Interpreter
    evaluator: Evaluator
    statement: str

    def __init__(self, statement: str):
        scanner = StatementScanner(statement)
        parser = Parser(scanner.scan_tokens())
        self.expression = parser.parse()
