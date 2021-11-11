from .token_type import TokenType


class Token:
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


# class Token {
#   final TokenType type;
#   final String lexeme;
#   final Object literal;
#   final int line;

#   Token(TokenType type, String lexeme, Object literal, int line) {
#     this.type = type;
#     this.lexeme = lexeme;
#     this.literal = literal;
#     this.line = line;
#   }

#   public String toString() {
#     return type + " " + lexeme + " " + literal;
#   }
# }
