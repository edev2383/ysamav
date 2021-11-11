from stockbox.stockbox.domain.rules.parser.token_category import TokenCategory
from stockbox.stockbox.domain.rules.parser.tv_factory import TVFactory
from .scanner_error import ScannerError, ScannerErrorList
from .token_list import TokenList
from .token_type import TokenType
import re


class IScanner:
    errors: ScannerErrorList
    tokens: TokenList
    source: str
    start: int = 0
    current: int = 0

    def __init__(self, source: str):
        self.source = source
        self.switch = ScannerSwitch(self)

    def scan_tokens(self):
        pass

    def scan_token(self):
        pass

    def add_simple_token(self, type: TokenType):
        pass

    def add_token(self, type: TokenType, lexeme: any):
        pass

    def is_at_end(self):
        pass

    def advance(self):
        return self.current >= len(self.source)

    def currpp(self):
        self.current = self.current + 1

    def curr_lexeme(self):
        return self.source[self.start : self.current]

    def curr_char(self):
        return self.source[self.current]

    def add_error(self, error: ScannerError):
        self.errors.append(error)

    def dump_errors(self):
        for err in self.errors:
            print(f"Error: {err.message}")


def case(char: str, type: TokenType):
    return char == type.value


class ScannerSwitch:
    """the logic of switching and recognizing tokens is encapsulated
    here, to allow the Scanner to act as a simple interface"""

    scanner: IScanner
    char: str
    re_digit = r"[0-9]"
    re_alpha = r"[a-zA-Z\_]"

    def __init__(self, scanner: IScanner):
        self.scanner = scanner

    def switch(self, char: str):
        self.char = char
        if case(self.char, TokenType.MINUS):
            self.add_simple(TokenType.MINUS)
            # -- these spaces are just to improve legibility. can remove
            # -- once the switch dev is finished
        elif case(self.char, TokenType.SPACE):
            pass
            #
        elif case(self.char, TokenType.RIGHT_PAREN):
            self.add_simple(TokenType.RIGHT_PAREN)
            #
        elif case(self.char, TokenType.LEFT_PAREN):
            self.add_simple(TokenType.LEFT_PAREN)
            #
        elif case(self.char, TokenType.LEFT_BRACE):
            self.add_simple(TokenType.LEFT_BRACE)
            #
        elif case(self.char, TokenType.RIGHT_BRACE):
            self.add_simple(TokenType.RIGHT_BRACE)
            #
        elif case(self.char, TokenType.SEMICOLON):
            self.add_simple(TokenType.SEMICOLON)
            #
        elif case(self.char, TokenType.STAR):
            self.add_simple(TokenType.STAR)
            #
        elif case(self.char, TokenType.COMMA):
            self.add_simple(TokenType.COMMA)
            #
        elif case(self.char, TokenType.COLON):
            self.add_simple(TokenType.COLON)
            #
        elif case(self.char, TokenType.PLUS):
            self.add_simple(TokenType.PLUS)
            #
        elif case(self.char, TokenType.DOT):
            self.add_simple(TokenType.DOT)
            #
        elif case(self.char, TokenType.SLASH):
            self.add_simple(TokenType.SLASH)
            #
        elif case(self.char, TokenType.CROSS_OVER):
            self.add_simple(TokenType.CROSS_OVER)
            #
        elif case(self.char, TokenType.LT):
            self.add_simple(self.caseLT())
            #
        elif case(self.char, TokenType.GT):
            self.add_simple(self.caseGT())
            #
        elif case(self.char, TokenType.EQ):
            self.add_simple(self.caseEQ())
            #
        elif case(self.char, TokenType.BANG):
            self.add_simple(self.caseBANG())
            #
        elif case(self.char, TokenType.IS):
            self.add_simple(TokenType.IS)
            #
        elif self.is_digit(self.char):
            self.caseNUMBER()
            #
        elif self.is_alpha(self.char):
            self.caseIDENTIFIER()
            #
        else:
            self._error(f"Unrecognized character: {char}")

    # ==================================================================
    # look ahead methods
    # ==================================================================
    def match(self, expected: str):
        if self.is_at_end():
            return False
        if self.curr_char() != expected:
            return False
        self.currpp()
        return True

    def peek(self):
        if self.is_at_end():
            return "\0"
        return self.curr_char()

    def peek_next(self):
        if self.curr() + 1 >= self.src_len():
            return "\0"
        return self.peak_next_src()

    # ==================================================================
    # char type identifier methods
    # ==================================================================
    def is_alphanumeric(self, char: str):
        return self.is_alpha(char) or self.is_digit(char)

    def is_alpha(self, char: str):
        m = re.match(self.re_alpha, char)
        return m is not None

    def is_digit(self, char: str):
        m = re.match(self.re_digit, char)
        return m is not None

    # ==================================================================
    # case logic
    # ==================================================================
    def caseIDENTIFIER(self):
        """case*** methods handle any case that is more than one char,
        including number, keywords, etc"""
        while self.is_alphanumeric(self.peek()):
            self.advance()
        lex = self.curr_lexeme().lower()
        if lex in set(i.value for i in TokenType):
            self.caseDOMAIN(TokenType(lex))
        else:
            # use case for IDENTIFIER remains to be seen, BUT could let
            # us allow more complex rules w/ proto-variables in future
            self.add_token(TokenType.IDENTIFIER, self.curr_lexeme())

    def caseDOMAIN(self, token: TokenType):
        # print(f"token: {token}")
        if token == TokenType.DAY or token == TokenType.DAYS:
            self.consume(TokenType.AGO)
            self.add_simple(TokenType.DOMAIN_INDEX)
            self.add_simple(TokenType.DAILY)
        elif token == TokenType.WEEK or token == TokenType.WEEKS:
            self.consume(TokenType.AGO)
            self.add_simple(TokenType.DOMAIN_INDEX)
            self.add_simple(TokenType.WEEKLY)
        elif token == TokenType.MONTH or token == TokenType.MONTHS:
            self.consume(TokenType.AGO)
            self.add_simple(TokenType.DOMAIN_INDEX)
            self.add_simple(TokenType.MONTHLY)
        else:
            tv = TVFactory.get(token)
            if tv.category == TokenCategory.INDICATOR:
                self.consume(TokenType.RIGHT_PAREN)
                self.add_token(token, self.curr_lexeme())
            else:
                self.add_token(token, self.curr_lexeme())

    def caseNUMBER(self):
        while self.is_digit(self.peek()):
            self.advance()
        if self.peek() == "." and self.is_digit(self.peek_next()):
            self.advance()
            while self.is_digit(self.peek()):
                self.advance()
        self.add_token(TokenType.NUMBER, float(self.curr_lexeme()))

    def caseEQ(self):
        return TokenType.EQEQ if self.match("=") else TokenType.EQ

    def caseBANG(self):
        return TokenType.BANG_EQ if self.match("=") else TokenType.BANG

    def caseLT(self):
        return TokenType.LT_OR_EQ if self.match("=") else TokenType.LT

    def caseGT(self):
        return TokenType.GT_OR_EQ if self.match("=") else TokenType.GT

    # ==================================================================
    # helpers to shorten interfacing with scanner parent. These remove
    # all scattered references to the parent from the execution code
    # above. This allows a more static interface should the scanner need
    # to change behavior
    # ==================================================================
    def add_simple(self, type: TokenType):
        self.scanner.add_simple_token(type)

    def curr_char(self):
        return self.scanner.curr_char()

    def curr_lexeme(self):
        return self.scanner.curr_lexeme()

    def curr(self):
        return self.scanner.current

    def src_len(self):
        return len(self.scanner.source)

    def advance(self):
        self.scanner.advance()

    def add_token(self, type: TokenType, lexeme: any):
        self.scanner.add_token(type, lexeme)

    def is_at_end(self):
        return self.scanner.is_at_end()

    def currpp(self):
        self.scanner.currpp()

    def peak_next_src(self):
        return self.scanner.source[self.curr() + 1]

    def _error(self, msg: str):
        """push the error message to the scanner.errors list"""
        self.scanner.add_error(ScannerError(msg))

    def consume(self, token: TokenType):
        while token.value.lower() not in self.curr_lexeme().lower():
            self.advance()
