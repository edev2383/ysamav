from stockbox.stockbox.domain.rules.parser.token_category import TokenCategory


class TokenValue:
    value: str
    category: TokenCategory

    def __init__(self, value: str, category: TokenCategory):
        self.value = value
        self.category = category
