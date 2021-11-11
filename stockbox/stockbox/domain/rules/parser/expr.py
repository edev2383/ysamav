from stockbox.stockbox.domain.rules.parser.token_category import TokenCategory
from stockbox.stockbox.domain.rules.parser.token_type import TokenType
from .abs_expr import AbstractExpr, ExprVisitor
from .token import Token


class Expr(AbstractExpr):
    left: AbstractExpr
    operator: Token
    right: AbstractExpr

    def __init__(self, left: AbstractExpr, op: Token, right: AbstractExpr):
        self.left = left
        self.operator = op
        self.right = right


class Binary(Expr):
    def accept(self, visitor: ExprVisitor):
        return visitor.visitBinary(self)


class Grouping(Expr):
    expression: Expr

    def __init__(self, expression: Expr):
        self.expression = expression

    def accept(self, visitor: ExprVisitor):
        return visitor.visitGrouping(self)


class Literal(Expr):
    value: object
    token: Token

    def __init__(self, value: object, token: Token = None):
        self.value = value
        self.token = token

    def accept(self, visitor: ExprVisitor):
        return visitor.visitLiteral(self)


class Unary(Expr):
    def __init__(self, operator: Token, right: Expr):
        self.operator = operator
        self.right = right

    def accept(self, visitor: ExprVisitor):
        return visitor.visitUnary(self)


class DomainBinary(Expr):
    pass

    def accept(self, visitor: ExprVisitor):
        ...


class Domain(Expr):
    column: object
    category: TokenCategory
    interval: TokenType

    def __init__(
        self,
        column: object,
        category: TokenCategory,
        interval: TokenType = TokenType.DAILY,
    ):
        self.column = column
        self.interval = interval
        self.category = category

    def accept(self, visitor: ExprVisitor):
        ...
