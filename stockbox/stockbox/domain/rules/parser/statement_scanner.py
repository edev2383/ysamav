from .scanner_error import ScannerErrorList
from .scanner_switch import ScannerSwitch, IScanner
from .token import Token
from .token_list import TokenList
from .token_type import TokenType


class StatementScanner(IScanner):
    source: str = ""
    start: int = 0
    current: int = 0

    def __init__(self, source: str):
        self.source = source
        self.tokens = TokenList()
        self.errors = ScannerErrorList()
        self.switch = ScannerSwitch(self)

    def scan_tokens(self):
        while self.is_at_end() == False:
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.start))
        return self.tokens

    def scan_token(self):
        c = self.advance()
        self.switch.switch(c)
        # tkn = TokenType(c)
        # if tkn:
        #     self.add_simple_token(tkn)
        # else:

    def add_simple_token(self, type: TokenType):
        txt = self.source[self.start : self.current]
        self.tokens.append(Token(type, txt, None, self.start))

    def add_token(self, type: TokenType, lexeme: any):
        self.tokens.append(Token(type, lexeme, None, self.start))

    def is_at_end(self):
        return self.current >= len(self.source)

    def advance(self):
        ret = self.source[self.current]
        self.currpp()
        return ret
