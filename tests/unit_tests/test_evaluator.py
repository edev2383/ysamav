from . import Evaluator
from . import Domain, DomainBinary
from . import TokenType
from . import StatementScanner
from . import Literal, Unary, Binary, Grouping
from . import Token
from . import Parser


def test_evaluator_truthy_method():
    evaluator = Evaluator()
    str_01 = "a"
    str_02 = ""
    bool_01 = True
    bool_02 = False
    none_01 = None
    obj_01 = StatementScanner("")
    assert evaluator._is_truthy(str_01) == True
    # EMPTY STRINGS EVALUATE TO FALSE FFSss
    assert evaluator._is_truthy(str_02) == False
    assert evaluator._is_truthy(bool_01) == True
    assert evaluator._is_truthy(bool_02) == False
    assert evaluator._is_truthy(none_01) == False
    assert evaluator._is_truthy(obj_01) == True


def test_evaluator_visit_unary_01():
    tkn = Token(TokenType.BANG, "!", None, 0)
    literal = Literal(True)
    unary = Unary(tkn, literal)
    evaluator = Evaluator(None)
    value = evaluator.evaluate(unary)
    assert value == False


def test_evaluator_visit_unary_02():
    tkn = Token(TokenType.MINUS, "-", None, 0)
    literal = Literal(20)
    unary = Unary(tkn, literal)
    evaluator = Evaluator(None)
    value = evaluator.evaluate(unary)
    assert value == -20


def test_evaluator_visit_unary_from_scanner_scr_alpha():
    src = StatementScanner("two days ago Close")
    tkns = src.scan_tokens()
    parser = Parser(tkns)
    expr = parser.parse()
    assert isinstance(expr, DomainBinary)
    assert isinstance(expr.left, Literal)
    assert expr.left.value == 2
    assert isinstance(expr.operator, Token)
    assert expr.operator.type == TokenType.DOMAIN_INDEX
    assert isinstance(expr.right, Domain)
    assert expr.right.column == "Close"
    assert isinstance(expr.right.interval, Token)
    assert expr.right.interval.type == TokenType.DAILY


def test_evaluator_visit_unary_from_scanner_scr_digit_01():
    src = StatementScanner("2 days ago Close")
    tkns = src.scan_tokens()
    parser = Parser(tkns)
    expr = parser.parse()
    assert isinstance(expr, DomainBinary)
    assert isinstance(expr.left, Literal)
    assert expr.left.value == 2
    assert isinstance(expr.operator, Token)
    assert expr.operator.type == TokenType.DOMAIN_INDEX
    assert isinstance(expr.right, Domain)
    assert expr.right.column == "Close"
    assert isinstance(expr.right.interval, Token)
    assert expr.right.interval.type == TokenType.DAILY


def test_evaluator_visit_unary_from_scanner_scr_digit_02():
    src = StatementScanner("2 weeks ago Close")
    tkns = src.scan_tokens()
    parser = Parser(tkns)
    expr = parser.parse()
    assert isinstance(expr, DomainBinary)
    assert isinstance(expr.left, Literal)
    assert expr.left.value == 2
    assert isinstance(expr.operator, Token)
    assert expr.operator.type == TokenType.DOMAIN_INDEX
    assert isinstance(expr.right, Domain)
    assert expr.right.column == "Close"
    assert isinstance(expr.right.interval, Token)
    assert expr.right.interval.type == TokenType.WEEKLY


def test_evaluator_visit_unary_from_scanner_scr_digit_03():
    src = StatementScanner("2 months ago Close")
    tkns = src.scan_tokens()
    parser = Parser(tkns)
    expr = parser.parse()
    assert isinstance(expr, DomainBinary)
    assert isinstance(expr.left, Literal)
    assert expr.left.value == 2
    assert isinstance(expr.operator, Token)
    assert expr.operator.type == TokenType.DOMAIN_INDEX
    assert isinstance(expr.right, Domain)
    assert expr.right.column == "Close"
    assert isinstance(expr.right.interval, Token)
    assert expr.right.interval.type == TokenType.MONTHLY


def test_evaluator_math_operations_01():
    src = "2 * 3 - 1 / 2"
    scanner = StatementScanner(src)
    tkns = scanner.scan_tokens()
    parser = Parser(tkns)
    expr = parser.parse()
    evaluator = Evaluator(None)
    value = evaluator.evaluate(expr)
    assert value == 5.5


def test_evaluator_math_operations_02():
    src = "2 + 3 - 1 + 1"
    scanner = StatementScanner(src)
    tkns = scanner.scan_tokens()
    parser = Parser(tkns)
    expr = parser.parse()
    evaluator = Evaluator(None)
    value = evaluator.evaluate(expr)
    assert value == 5.0


def test_evaluator_comparison_operations_01():
    src = "6 == 6"
    scanner = StatementScanner(src)
    tkns = scanner.scan_tokens()
    parser = Parser(tkns)
    expr = parser.parse()
    evaluator = Evaluator(None)
    value = evaluator.evaluate(expr)
    assert value == True


def test_evaluator_comparison_operations_02():
    src = "5 < 7"
    scanner = StatementScanner(src)
    tkns = scanner.scan_tokens()
    parser = Parser(tkns)
    expr = parser.parse()
    evaluator = Evaluator(None)
    value = evaluator.evaluate(expr)
    assert value == True


def test_evaluator_comparison_operations_03():
    src = "9 >= 7"
    scanner = StatementScanner(src)
    tkns = scanner.scan_tokens()
    parser = Parser(tkns)
    expr = parser.parse()
    evaluator = Evaluator(None)
    value = evaluator.evaluate(expr)
    assert value == True


def test_evaluator_comparison_operations_04():
    src = "1 != 2"
    scanner = StatementScanner(src)
    tkns = scanner.scan_tokens()
    parser = Parser(tkns)
    expr = parser.parse()
    evaluator = Evaluator(None)
    value = evaluator.evaluate(expr)
    assert value == True


def test_evaluator_comparison_operations_05():
    src = "1 == 2"
    scanner = StatementScanner(src)
    tkns = scanner.scan_tokens()
    parser = Parser(tkns)
    expr = parser.parse()
    evaluator = Evaluator(None)
    value = evaluator.evaluate(expr)
    assert value == False
