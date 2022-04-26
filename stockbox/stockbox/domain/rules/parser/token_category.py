from enum import Enum


class TokenCategory(Enum):
    """ This is some additional metadata wrapped around the token"""
    KEYWORD = "keyword"
    OPERATOR = "operator"
    COMPARISON = "comparison"
    GENERIC = "generic"

    LOGIC = "logic"

    # domain
    DOMAIN_KEYWORD = "domain_keyword"
    TIMEFRAME = "timeframe"
    TIMEFRAME_NUMBER = "timeframe_number"
    INDICATOR = "indicator"
    INTERVAL = "interval"  # i.e., WEEKLY, MONTHLY, etc

    # type
    NUMBER = "number"
    STRING = "string"
    BOOLEAN = "boolean"
    NONE = "none"

    IDENTIFIER = "identifier"
