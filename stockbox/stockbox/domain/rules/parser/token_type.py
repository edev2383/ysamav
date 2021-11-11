from enum import Enum


class TokenType(Enum):
    # ==================================================================
    # Generic tokens
    # ==================================================================
    MINUS = "-"
    SPACE = " "
    RIGHT_PAREN = ")"
    LEFT_PAREN = "("
    LEFT_BRACE = "{"
    RIGHT_BRACE = "}"
    SEMICOLON = ";"
    STAR = "*"
    COMMA = ","
    COLON = ":"
    PLUS = "+"
    DOT = "."
    SLASH = "/"

    # ==================================================================
    # Comparison tokens
    # ==================================================================
    CROSS_OVER = "x"
    LT = "<"
    LT_OR_EQ = "<="
    GT = ">"
    GT_OR_EQ = ">="
    EQ = "="
    EQEQ = "=="
    BANG = "!"
    BANG_EQ = "!="
    IS = "is"
    EOF = "eof"

    # ==================================================================
    # non-domain specific reserved words
    # ==================================================================
    AND = "and"
    OR = "or"
    IF = "if"
    ELSE = "else"

    # ==================================================================
    # domain related reserved words
    # ==================================================================
    CLOSE = "close"
    ADJCLOSE = "adjclose"
    HIGH = "high"
    LOW = "low"
    OPEN = "open"
    VOLUME = "volume"

    DOMAIN_INDEX = "d~"

    # ==================================================================
    # timeframe reserved words
    # ==================================================================
    DAY = "day"
    DAYS = "days"
    WEEKS = "weeks"
    WEEK = "week"
    MONTHS = "months"
    MONTH = "month"
    YEAR = "year"
    YEARS = "years"
    AGO = "ago"
    # ==================================================================
    # numeric words
    # ==================================================================
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    DAILY = "daily"

    # ==================================================================
    # numeric words
    # ==================================================================
    ONE = "one"
    TWO = "two"
    THREE = "three"
    FOUR = "four"
    FIVE = "five"
    SIX = "six"
    SEVEN = "seven"
    EIGHT = "eight"
    NINE = "nine"
    TEN = "ten"

    # ==================================================================
    # indicators
    # ==================================================================
    SMA = "sma"
    SLOSTO = "slosto"
    SLOWSTO = "slowsto"

    # ==================================================================
    # type
    # ==================================================================
    NUMBER = "n~"
    STRING = "str~"

    # ==================================================================
    # variable identifiers
    # ==================================================================
    IDENTIFIER = "id~"

    FALSE = "false"
    TRUE = "true"
    NIL = "nil"


# class TokenType(Enum):
#     # ==================================================================
#     # Generic tokens
#     # ==================================================================
#     SPACE = TokenCategory.GENERIC
#     RIGHT_PAREN = TokenCategory.GENERIC
#     LEFT_PAREN = TokenCategory.GENERIC
#     LEFT_BRACE = TokenCategory.GENERIC
#     RIGHT_BRACE = TokenCategory.GENERIC
#     SEMICOLON = TokenCategory.GENERIC
#     COMMA = TokenCategory.GENERIC
#     COLON = TokenCategory.GENERIC
#     DOT = TokenCategory.GENERIC

#     STAR = TokenCategory.OPERATOR
#     MINUS = TokenCategory.OPERATOR
#     SLASH = TokenCategory.OPERATOR
#     PLUS = TokenCategory.OPERATOR
#     # ==================================================================
#     # Comparison tokens
#     # ==================================================================
#     CROSS_OVER = TokenCategory.COMPARISON
#     LT = TokenCategory.COMPARISON
#     LT_OR_EQ = TokenCategory.COMPARISON
#     GT = TokenCategory.COMPARISON
#     GT_OR_EQ = TokenCategory.COMPARISON
#     EQ = TokenCategory.COMPARISON
#     EQEQ = TokenCategory.COMPARISON
#     BANG = TokenCategory.COMPARISON
#     BANG_EQ = TokenCategory.COMPARISON

#     IS = TokenCategory.GENERIC
#     EOF = TokenCategory.GENERIC

#     # ==================================================================
#     # non-domain specific reserved words
#     # ==================================================================
#     AND = TokenCategory.LOGIC
#     OR = TokenCategory.LOGIC
#     IF = TokenCategory.LOGIC
#     ELSE = TokenCategory.LOGIC

#     # ==================================================================
#     # domain related reserved words
#     # ==================================================================
#     CLOSE = TokenCategory.DOMAIN_KEYWORD
#     HIGH = TokenCategory.DOMAIN_KEYWORD
#     LOW = TokenCategory.DOMAIN_KEYWORD
#     OPEN = TokenCategory.DOMAIN_KEYWORD
#     VOLUME = TokenCategory.DOMAIN_KEYWORD

#     # ==================================================================
#     # timeframe reserved words
#     # ==================================================================
#     DAY = TokenCategory.TIMEFRAME
#     DAYS = TokenCategory.TIMEFRAME
#     AGO = TokenCategory.TIMEFRAME

#     # ==================================================================
#     # numeric words
#     # ==================================================================
#     ONE = TokenCategory.TIMEFRAME_NUMBER
#     TWO = TokenCategory.TIMEFRAME_NUMBER
#     THREE = TokenCategory.TIMEFRAME_NUMBER
#     FOUR = TokenCategory.TIMEFRAME_NUMBER
#     FIVE = TokenCategory.TIMEFRAME_NUMBER
#     SIX = TokenCategory.TIMEFRAME_NUMBER
#     SEVEN = TokenCategory.TIMEFRAME_NUMBER
#     EIGHT = TokenCategory.TIMEFRAME_NUMBER
#     NINE = TokenCategory.TIMEFRAME_NUMBER
#     TEN = TokenCategory.TIMEFRAME_NUMBER

#     # ==================================================================
#     # indicators
#     # ==================================================================
#     SMA = TokenCategory.INDICATOR
#     SLOSTO = TokenCategory.INDICATOR
#     SLOWSTO = TokenCategory.INDICATOR

#     # ==================================================================
#     # type
#     # ==================================================================
#     NUMBER = TokenCategory.NUMBER
#     STRING = TokenCategory.STRING

#     # ==================================================================
#     # variable identifiers
#     # ==================================================================
#     IDENTIFIER = TokenCategory.IDENTIFIER

#     FALSE = TokenCategory.BOOLEAN
#     TRUE = TokenCategory.BOOLEAN
#     NIL = TokenCategory.NONE

# ==================================================================
# Generic tokens
# ==================================================================
# SPACE = TokenValue(" ", TokenCategory.GENERIC)
# RIGHT_PAREN = TokenValue(")", TokenCategory.GENERIC)
# LEFT_PAREN = TokenValue("(", TokenCategory.GENERIC)
# LEFT_BRACE = TokenValue("{", TokenCategory.GENERIC)
# RIGHT_BRACE = TokenValue("}", TokenCategory.GENERIC)
# SEMICOLON = TokenValue(";", TokenCategory.GENERIC)
# COMMA = TokenValue(",", TokenCategory.GENERIC)
# COLON = TokenValue(":", TokenCategory.GENERIC)
# DOT = TokenValue(".", TokenCategory.GENERIC)
# IS = TokenValue("is", TokenCategory.GENERIC)
# EOF = TokenValue("eof", TokenCategory.GENERIC)

# # ==================================================================
# # Operator tokens
# # ==================================================================
# STAR = TokenValue("*", TokenCategory.OPERATOR)
# SLASH = TokenValue("/", TokenCategory.OPERATOR)
# PLUS = TokenValue("+", TokenCategory.OPERATOR)
# MINUS = TokenValue("-", TokenCategory.OPERATOR)

# # ==================================================================
# # Comparison tokens
# # ==================================================================
# CROSS_OVER = TokenValue("x", TokenCategory.COMPARISON)
# LT = TokenValue("<", TokenCategory.COMPARISON)
# LT_OR_EQ = TokenValue("<=", TokenCategory.COMPARISON)
# GT = TokenValue(">", TokenCategory.COMPARISON)
# GT_OR_EQ = TokenValue(">=", TokenCategory.COMPARISON)
# EQ = TokenValue("=", TokenCategory.COMPARISON)
# EQEQ = TokenValue("==", TokenCategory.COMPARISON)
# BANG = TokenValue("!", TokenCategory.COMPARISON)
# BANG_EQ = TokenValue("!=", TokenCategory.COMPARISON)

# # ==================================================================
# # non-domain specific reserved words
# # ==================================================================
# AND = TokenValue("and", TokenCategory.LOGIC)
# OR = TokenValue("or", TokenCategory.LOGIC)
# IF = TokenValue("if", TokenCategory.LOGIC)
# ELSE = TokenValue("else", TokenCategory.LOGIC)

# # ==================================================================
# # domain related reserved words
# # ==================================================================
# CLOSE = TokenValue("close", TokenCategory.DOMAIN_KEYWORD)
# HIGH = TokenValue("high", TokenCategory.DOMAIN_KEYWORD)
# LOW = TokenValue("low", TokenCategory.DOMAIN_KEYWORD)
# OPEN = TokenValue("open", TokenCategory.DOMAIN_KEYWORD)
# VOLUME = TokenValue("volume", TokenCategory.DOMAIN_KEYWORD)

# # ==================================================================
# # timeframe reserved words
# # ==================================================================
# DAY = TokenValue("day", TokenCategory.TIMEFRAME)
# DAYS = TokenValue("days", TokenCategory.TIMEFRAME)
# AGO = TokenValue("ago", TokenCategory.TIMEFRAME)

# # ==================================================================
# # numeric words
# # ==================================================================
# ONE = TokenValue("one", TokenCategory.TIMEFRAME_NUMBER)
# TWO = TokenValue("two", TokenCategory.TIMEFRAME_NUMBER)
# THREE = TokenValue("three", TokenCategory.TIMEFRAME_NUMBER)
# FOUR = TokenValue("four", TokenCategory.TIMEFRAME_NUMBER)
# FIVE = TokenValue("five", TokenCategory.TIMEFRAME_NUMBER)
# SIX = TokenValue("six", TokenCategory.TIMEFRAME_NUMBER)
# SEVEN = TokenValue("seven", TokenCategory.TIMEFRAME_NUMBER)
# EIGHT = TokenValue("eight", TokenCategory.TIMEFRAME_NUMBER)
# NINE = TokenValue("nine", TokenCategory.TIMEFRAME_NUMBER)
# TEN = TokenValue("ten", TokenCategory.TIMEFRAME_NUMBER)

# # ==================================================================
# # indicators
# # ==================================================================
# SMA = TokenValue("sma", TokenCategory.INDICATOR)
# SLOSTO = TokenValue("slosto", TokenCategory.INDICATOR)
# SLOWSTO = TokenValue("slowsto", TokenCategory.INDICATOR)

# # ==================================================================
# # type
# # ==================================================================
# NUMBER = TokenValue("n~", TokenCategory.NUMBER)
# STRING = TokenValue("str~", TokenCategory.STRING)

# # ==================================================================
# # variable identifiers
# # ==================================================================
# IDENTIFIER = TokenValue("id~", TokenCategory.IDENTIFIER)

# FALSE = TokenValue("false", TokenCategory.BOOLEAN)
# TRUE = TokenValue("true", TokenCategory.BOOLEAN)
# NIL = TokenValue("nil", TokenCategory.NONE)
