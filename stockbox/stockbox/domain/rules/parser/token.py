from .token_type import TokenType


class Token:
    """As the parser recognizes collections of characters as cohesive units, 
    they become Tokens. Using these tokens, we can then assign values that can
    be evaluated for our rules"""
    type: TokenType
    lexeme: str
    literal: object
    char: int

    def __init__(self, type: TokenType, lexeme: str, literal: object, char: int):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.char = char

    def to_string(self):
        return f"{self.type} {self.lexeme} {self.literal} char: {self.char}"
