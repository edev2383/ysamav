from stockbox.stockbox.common.helpers.enums import ETickerRequestFrequency, EResult
from stockbox.stockbox.domain.rules.parser.evaluators.evaluator import Evaluator
from stockbox.stockbox.domain.rules.parser.expr import Domain, DomainBinary, Unary
from stockbox.stockbox.services.ticker.ticker import Ticker
from . import Binary, Literal
from . import Rule
from . import Token, TokenType
from .fakes.fake_ticker import FakeTicker


def test_rule_will_add_missing_indicator():
    src = "2 days ago Close < SMA(2)"
    ticker = FakeTicker()
    rule = Rule(src)
    rule.add_ticker(ticker)
    eval = Evaluator(ticker)
    assert isinstance(rule.expression, Binary)
    assert eval.evaluate(rule.expression.left)
    value = rule.process()
    assert _found_indicator("SMA(2)", ticker, ETickerRequestFrequency.eDaily)
    # Rule.process returns a Result obj
    return value.status == EResult.eSuccess


# ======================================================================
# Test that the rules are evaluating correctly
# ======================================================================
def test_rule_evaluation_01():
    src = "2 days ago Close < Open"
    ticker = FakeTicker()
    rule = Rule(src)
    rule.add_ticker(ticker)
    eval = Evaluator(FakeTicker())
    assert isinstance(rule.expression, Binary)
    left = eval.evaluate(rule.expression.left)
    assert left == 10
    right = eval.evaluate(rule.expression.right)
    assert right == 7
    value = rule.process()
    # Rule.process returns a Result obj
    assert value.status == EResult.eFail


def test_rule_evaluation_02():
    src = "Close > Open"
    ticker = FakeTicker()
    rule = Rule(src)
    rule.add_ticker(ticker)
    eval = Evaluator(FakeTicker())
    assert isinstance(rule.expression, Binary)
    left = eval.evaluate(rule.expression.left)
    assert left == 8
    right = eval.evaluate(rule.expression.right)
    assert right == 7
    value = rule.process()
    # Rule.process returns a Result obj
    assert value.status == EResult.eSuccess


def test_rule_evaluation_03():
    src = "three days ago High < 2 days ago Low"
    ticker = FakeTicker()
    rule = Rule(src)
    rule.add_ticker(ticker)
    eval = Evaluator(FakeTicker())
    assert isinstance(rule.expression, Binary)
    left = eval.evaluate(rule.expression.left)
    assert left == 12
    right = eval.evaluate(rule.expression.right)
    assert right == 8
    value = rule.process()
    # Rule.process returns a Result obj
    assert value.status == EResult.eFail


def test_rule_evaluation_04():
    src = "2 days ago Open < 4 days ago Open"
    ticker = FakeTicker()
    rule = Rule(src)
    rule.add_ticker(ticker)
    eval = Evaluator(FakeTicker())
    assert isinstance(rule.expression, Binary)
    left = eval.evaluate(rule.expression.left)
    assert left == 9
    right = eval.evaluate(rule.expression.right)
    assert right == 11
    value = rule.process()
    # Rule.process returns a Result obj
    assert value.status == EResult.eSuccess


def test_rule_evaluation_05():
    src = "5 <  Open"
    ticker = FakeTicker()
    rule = Rule(src)
    rule.add_ticker(ticker)
    eval = Evaluator(FakeTicker())
    assert isinstance(rule.expression, Binary)
    left = eval.evaluate(rule.expression.left)
    assert left == 5
    right = eval.evaluate(rule.expression.right)
    assert right == 7
    value = rule.process()
    # Rule.process returns a Result obj
    assert value.status == EResult.eSuccess


def test_rule_evaluation_06():
    src = "Two days ago Close > 4"
    ticker = FakeTicker()
    rule = Rule(src)
    rule.add_ticker(ticker)
    eval = Evaluator(FakeTicker())
    assert isinstance(rule.expression, Binary)
    left = eval.evaluate(rule.expression.left)
    assert left == 10
    right = eval.evaluate(rule.expression.right)
    assert right == 4
    value = rule.process()
    # Rule.process returns a Result obj
    assert value.status == EResult.eSuccess


# ======================================================================
# Test that the rule expression return the expected Expr instances and
# are parsed correctly
# ======================================================================
def test_rule_expression_01():
    src = "Close < Open"
    ticker = FakeTicker()
    rule = Rule(src)
    rule.add_ticker(ticker)
    expr = rule.expression
    assert isinstance(expr, Binary)
    assert isinstance(expr.left, Domain)
    assert isinstance(expr.operator, Token)
    assert isinstance(expr.right, Domain)
    assert expr.left.column == "Close"
    assert expr.right.column == "Open"
    assert expr.operator.type == TokenType.LT


def test_rule_expression_02():
    src = "2 days ago Close > High"
    ticker = FakeTicker()
    rule = Rule(src)
    rule.add_ticker(ticker)
    expr = rule.expression
    assert isinstance(expr, Binary)
    assert isinstance(expr.operator, Token)
    assert expr.operator.type == TokenType.GT
    assert isinstance(expr.right, Domain)
    assert expr.right.column == "High"
    # ! ========== Test Left Binary Expression
    left_expr = expr.left
    assert isinstance(left_expr, DomainBinary)
    assert isinstance(left_expr.left, Literal)
    assert isinstance(left_expr.operator, Token)
    assert left_expr.operator.type == TokenType.DOMAIN_INDEX
    assert isinstance(left_expr.right, Domain)
    assert left_expr.right.column == "Close"


def test_rule_expression_03():
    src = "2 days ago Close > SMA(25)"
    ticker = FakeTicker()
    rule = Rule(src)
    rule.add_ticker(ticker)
    expr = rule.expression
    assert isinstance(expr, Binary)
    assert isinstance(expr.operator, Token)
    assert expr.operator.type == TokenType.GT
    # ! ========== Test Right Binary Indicator
    assert isinstance(expr.right, Literal)
    assert expr.right.value == "SMA(25)"
    # ! ========== Test Left Binary Expression
    left_expr = expr.left
    assert isinstance(left_expr, Binary)
    assert isinstance(left_expr.left, Literal)
    assert isinstance(left_expr.operator, Token)
    assert left_expr.operator.type == TokenType.DOMAIN_INDEX
    assert isinstance(left_expr.right, Unary)
    rt_unary = left_expr.right
    assert isinstance(rt_unary.operator, Token)
    assert rt_unary.operator.type == TokenType.DAILY
    assert isinstance(rt_unary.right, Literal)
    assert rt_unary.right.value == "Close"


def test_rule_expression_03():
    src = "8 days ago High > SlowSto(14,3)"
    ticker = FakeTicker()
    rule = Rule(src)
    rule.add_ticker(ticker)
    expr = rule.expression
    assert isinstance(expr, Binary)
    assert isinstance(expr.operator, Token)
    assert expr.operator.type == TokenType.GT
    # ! ========== Test Right Binary Indicator
    assert isinstance(expr.right, Domain)
    assert expr.right.column == "SlowSto(14,3)"
    # ! ========== Test Left Binary Expression
    left_expr = expr.left
    assert isinstance(left_expr, DomainBinary)
    assert isinstance(left_expr.left, Literal)
    assert isinstance(left_expr.operator, Token)
    assert left_expr.operator.type == TokenType.DOMAIN_INDEX
    assert isinstance(left_expr.right, Domain)
    rt_dom = left_expr.right
    assert isinstance(rt_dom.interval, Token)
    assert rt_dom.interval.type == TokenType.DAILY
    assert rt_dom.column == "High"


def _found_indicator(key: str, ticker: Ticker, i: ETickerRequestFrequency):
    collection = ticker._indicators.parse_target(i).col
    for ind in collection:
        if ind.df_colkey == key:
            return True
    return False
