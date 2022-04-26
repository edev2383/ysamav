from stockbox.stockbox.domain.rules.parser.token_value import TokenValue
from .token_category import TokenCategory as TCat
from .token_type import TokenType as TType

tv_map = {}

"""We needed to assign more value to the tokens, specifically we wanted to wrap
a category value around them, to relate types of tokens together. tv_map is then
called statically by TVFactory.get(token) to get the category of a token type
passed"""


def add_tv(type: TType, category: TCat):
    tv_map[type] = TokenValue(type.value, category)


add_tv(TType.SPACE, TCat.GENERIC)
add_tv(TType.RIGHT_PAREN, TCat.GENERIC)
add_tv(TType.LEFT_PAREN, TCat.GENERIC)
add_tv(TType.RIGHT_BRACE, TCat.GENERIC)
add_tv(TType.LEFT_BRACE, TCat.GENERIC)
add_tv(TType.SEMICOLON, TCat.GENERIC)
add_tv(TType.COMMA, TCat.GENERIC)
add_tv(TType.COLON, TCat.GENERIC)
add_tv(TType.DOT, TCat.GENERIC)
add_tv(TType.IS, TCat.GENERIC)
add_tv(TType.EOF, TCat.GENERIC)

add_tv(TType.STAR, TCat.OPERATOR)
add_tv(TType.MINUS, TCat.OPERATOR)
add_tv(TType.SLASH, TCat.OPERATOR)
add_tv(TType.PLUS, TCat.OPERATOR)
add_tv(TType.DOMAIN_INDEX, TCat.OPERATOR)

add_tv(TType.CROSS_OVER, TCat.COMPARISON)
add_tv(TType.LT, TCat.COMPARISON)
add_tv(TType.LT_OR_EQ, TCat.COMPARISON)
add_tv(TType.GT, TCat.COMPARISON)
add_tv(TType.GT_OR_EQ, TCat.COMPARISON)
add_tv(TType.EQ, TCat.COMPARISON)
add_tv(TType.EQEQ, TCat.COMPARISON)
add_tv(TType.BANG, TCat.COMPARISON)
add_tv(TType.BANG_EQ, TCat.COMPARISON)

add_tv(TType.AND, TCat.LOGIC)
add_tv(TType.OR, TCat.LOGIC)
add_tv(TType.IF, TCat.LOGIC)
add_tv(TType.ELSE, TCat.LOGIC)

add_tv(TType.CLOSE, TCat.DOMAIN_KEYWORD)
add_tv(TType.HIGH, TCat.DOMAIN_KEYWORD)
add_tv(TType.LOW, TCat.DOMAIN_KEYWORD)
add_tv(TType.OPEN, TCat.DOMAIN_KEYWORD)
add_tv(TType.VOLUME, TCat.DOMAIN_KEYWORD)
add_tv(TType.ADJCLOSE, TCat.DOMAIN_KEYWORD)

add_tv(TType.DAY, TCat.TIMEFRAME)
add_tv(TType.DAYS, TCat.TIMEFRAME)
add_tv(TType.WEEK, TCat.TIMEFRAME)
add_tv(TType.WEEKS, TCat.TIMEFRAME)
add_tv(TType.MONTH, TCat.TIMEFRAME)
add_tv(TType.MONTHS, TCat.TIMEFRAME)
add_tv(TType.YEAR, TCat.TIMEFRAME)
add_tv(TType.YEARS, TCat.TIMEFRAME)
add_tv(TType.AGO, TCat.TIMEFRAME)

add_tv(TType.ONE, TCat.TIMEFRAME_NUMBER)
add_tv(TType.TWO, TCat.TIMEFRAME_NUMBER)
add_tv(TType.THREE, TCat.TIMEFRAME_NUMBER)
add_tv(TType.FOUR, TCat.TIMEFRAME_NUMBER)
add_tv(TType.FIVE, TCat.TIMEFRAME_NUMBER)
add_tv(TType.SIX, TCat.TIMEFRAME_NUMBER)
add_tv(TType.SEVEN, TCat.TIMEFRAME_NUMBER)
add_tv(TType.EIGHT, TCat.TIMEFRAME_NUMBER)
add_tv(TType.NINE, TCat.TIMEFRAME_NUMBER)
add_tv(TType.TEN, TCat.TIMEFRAME_NUMBER)

add_tv(TType.SMA, TCat.INDICATOR)
add_tv(TType.SLOSTO, TCat.INDICATOR)
add_tv(TType.SLOWSTO, TCat.INDICATOR)

add_tv(TType.NUMBER, TCat.NUMBER)
add_tv(TType.STRING, TCat.STRING)

add_tv(TType.FALSE, TCat.BOOLEAN)
add_tv(TType.TRUE, TCat.BOOLEAN)

add_tv(TType.NIL, TCat.NONE)

add_tv(TType.IDENTIFIER, TCat.IDENTIFIER)

add_tv(TType.DAILY, TCat.INTERVAL)
add_tv(TType.WEEKLY, TCat.INTERVAL)
add_tv(TType.MONTHLY, TCat.INTERVAL)


class TVFactory:
    @staticmethod
    def get(type: TType) -> TokenValue:
        # print(f"type: {type.value}")
        if type is None:
            return tv_map[TType.EOF]
        return tv_map[type]
