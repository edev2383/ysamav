from stockbox.stockbox.domain.rules.parser.expr import (
    Binary,
    Domain,
    DomainBinary,
    Grouping,
    Literal,
    Unary,
)
from . import StatementScanner, Token, TokenType, Parser


def test_parser_can_be_created():
    src = "Close < SMA(50)"
    s = _scn(src)
    tkns = s.scan_tokens()
    parser = Parser(tkns)
    assert parser is not None


def test_parser_creates_expression():
    src = "1 + (2 * 8)"
    scanner = _scn(src)
    tkns = scanner.scan_tokens()
    parser = Parser(tkns)
    assert parser is not None
    expr = parser.parse()
    assert isinstance(expr, Binary)
    assert isinstance(expr.left, Literal)
    assert isinstance(expr.operator, Token)
    assert expr.operator.type == TokenType.PLUS
    # ! Test the parenthesis create a GROUPING
    assert isinstance(expr.right, Grouping)
    grp_expr = expr.right.expression
    assert isinstance(grp_expr, Binary)
    assert isinstance(grp_expr.left, Literal)
    assert isinstance(grp_expr.operator, Token)
    assert isinstance(grp_expr.right, Literal)
    assert grp_expr.left.value == 2
    assert grp_expr.operator.type == TokenType.STAR
    assert grp_expr.right.value == 8


def test_parser_can_recognize_domain_tokens():
    src = "Close < High"
    s = _scn(src)
    p = Parser(s.scan_tokens())
    expr = p.parse()
    assert p is not None
    assert isinstance(p, Parser)
    assert isinstance(expr, Binary)
    assert isinstance(expr.left, Domain)
    assert expr.left.column == "Close"
    assert isinstance(expr.operator, Token)
    assert expr.operator.type == TokenType.LT
    assert isinstance(expr.right, Domain)
    assert expr.right.column == "High"


def test_parser_can_recognize_domain_expression():
    src = "two days ago Close < High"
    s = _scn(src)
    parser = Parser(s.scan_tokens())
    expr = parser.parse()
    assert parser is not None
    assert isinstance(parser, Parser)
    # ! ================= Test the MAIN EXPRESSION
    assert isinstance(expr, Binary)
    assert isinstance(expr.left, DomainBinary)
    assert isinstance(expr.operator, Token)
    assert expr.operator.type == TokenType.LT
    assert expr.right.column == "High"
    # ! ================= Test the LEFT BINARY
    left_expr = expr.left
    assert isinstance(left_expr.left, Literal)
    assert isinstance(left_expr.operator, Token)
    assert isinstance(left_expr.right, Domain)
    assert left_expr.left.value == 2
    assert left_expr.operator.type == TokenType.DOMAIN_INDEX
    rt_dom = left_expr.right
    assert rt_dom.interval.type == TokenType.DAILY
    assert rt_dom.column == "Close"


def _scn(src: str):
    return StatementScanner(src)


def _tkns(src: str):
    scanner = _scn(src)
    return scanner.scan_tokens()


def _debug_tkns(tkns, bool=True):
    if bool is True:
        print("")
        print("--- DEBUG ----")
        for t in tkns:
            print(t.to_string())
        print("--- END DEBUG ----")
        print("")
