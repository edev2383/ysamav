from stockbox.stockbox.domain.rules.parser.token import Token
from stockbox.stockbox.domain.rules.parser.token_category import TokenCategory
from stockbox.stockbox.domain.rules.parser.tv_factory import TVFactory
from .expr import Binary, DomainBinary, Expr, Grouping, Unary, Literal, Domain
from .token_list import TokenList
from .token_type import TokenType as TType


class Parser:
    tokens: TokenList
    current: int = 0
    steps: list

    def __init__(self, tokens: TokenList):
        self.tokens = tokens
        # for debugging
        self.steps = []

    def _log(self, msg):
        self.steps.append(msg)

    # ==================================================================
    # Public interface
    # ==================================================================
    def parse(self) -> Expr:
        try:
            return self.expression()
        except ValueError:
            return None

    # ==================================================================
    # Evaluation methods
    # ==================================================================
    def expression(self) -> Expr:
        return self.equality()

    def equality(self) -> Expr:
        expr = self.comparison()
        while self.match(TType.BANG_EQ, TType.EQEQ):
            self._log("equality")
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)
        return expr

    def comparison(self) -> Expr:
        expr = self.term()
        while self.match(TType.GT, TType.GT_OR_EQ, TType.LT, TType.LT_OR_EQ):
            self._log("comparison")
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)
        return expr

    def is_domain_token(self) -> bool:
        curr = self.peek()
        token_value = TVFactory.get(curr.type)
        if token_value.category == TokenCategory.DOMAIN_KEYWORD:
            self.advance()
            return True

    def is_indicator_token(self) -> bool:
        curr = self.peek()
        token_value = TVFactory.get(curr.type)
        if token_value.category == TokenCategory.INDICATOR:
            self.advance()
            return True
        return False

    def is_timeframe_number(self) -> bool:
        curr = self.peek()
        token_value = TVFactory.get(curr.type)
        if token_value.category == TokenCategory.TIMEFRAME_NUMBER:
            self.advance()
            return True
        return False

    def term(self) -> Expr:
        expr = self.factor()

        while self.match(TType.MINUS, TType.PLUS):
            self._log("term minus/plus")

            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)
        return expr

    def factor(self) -> Expr:
        expr = self.unary()
        while self.match(TType.DOMAIN_INDEX, TType.SLASH, TType.STAR):
            self._log("factor")
            operator = self.previous()
            if operator.type == TType.DOMAIN_INDEX:
                right = self.unary()
                expr = DomainBinary(expr, operator, right)
            else:
                right = self.unary()
                expr = Binary(expr, operator, right)
        return expr

    def unary(self) -> Expr:
        if self.match(TType.DAILY, TType.WEEKLY, TType.MONTHLY):
            self._log("unary domain interval")
            interval = self.previous()
            column = self.peek().lexeme
            tv = TVFactory.get(self.peek().type)
            self.advance()
            return Domain(column=column, interval=interval, category=tv.category)
        if self.match(TType.BANG, TType.MINUS):
            self._log("unary bang/minus")
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)
        return self.primary()

    def primary(self) -> Expr:
        if self.is_domain_token():
            self._log("domain_token")
            tkn = self.previous()
            return Domain(column=tkn.lexeme, category=TokenCategory.DOMAIN_KEYWORD)
        if self.is_indicator_token():
            self._log("indicator token")
            tkn = self.previous()
            return Domain(column=tkn.lexeme, category=TokenCategory.INDICATOR)
        if self.is_timeframe_number():
            self._log("timeframe number")
            num = self.previous()
            return Literal(self.map_num(num.lexeme))
        if self.match(TType.FALSE):
            self._log("literal bool false")
            return Literal(False)
        if self.match(TType.TRUE):
            self._log("literal bool true")
            return Literal(True)
        if self.match(TType.NIL):
            self._log("literal nil")
            return Literal(None)
        if self.match(TType.NUMBER, TType.STRING):
            self._log("litearl num string")
            return Literal(self.previous().lexeme, self.previous())
        if self.match(TType.LEFT_PAREN):
            self._log("grouping")
            expr = self.expression()
            self.consume(TType.RIGHT_PAREN, "Expect ')' after expression.")
            return Grouping(expr)

    def consume(self, type: TType, message: str):
        if self.check(type):
            return self.advance()
        raise self.error(self.peek(), message)

    def error(self, type: TType, message: str) -> ValueError:
        return ValueError(message)

    # ==================================================================
    # State methods
    # ==================================================================
    def is_at_end(self) -> bool:
        return self.peek().type == TType.EOF

    def advance(self) -> Token:
        if self.is_at_end() is False:
            self.currpp()
        return self.previous()

    # ==================================================================
    # Look ahead methods
    # ==================================================================
    def peek(self) -> Token:
        return self.tokens[self.current]

    def peeknext(self) -> Token:
        return self.tokens[self.current + 1]

    def currpp(self) -> None:
        self.current = self.current + 1

    def previous(self) -> Token:
        return self.tokens[self.current - 1]

    def match(self, *args) -> bool:
        for type in args:
            if self.check(type) is True:
                self.advance()
                return True
        return False

    def check(self, type: TType) -> bool:
        if self.is_at_end():
            return False
        return self.peek().type == type

    def map_num(self, num: str) -> int:
        v = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight"]
        if num.lower() in v:
            return v.index(num.lower())
        return 0
